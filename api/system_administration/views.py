from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse
import openpyxl
from drf_spectacular.utils import extend_schema_view, extend_schema
from appdata.models import CourseRegistration, Course, UploadHistory, SessionRegistration, AcademicSession
from appdata.models.enums.choices import ParseStatus
from api.system_administration.serializers import UploadHistorySerializer, UploadResponseSerializer

@extend_schema_view(
    get=extend_schema(
        summary='Generate score sheet template',
        description='Generate an Excel template for uploading scores for a given session and course',
        tags=['Score Sheet Upload'],
        responses={
            200: 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
            400: {'description': 'Invalid session or course'}
        }
    )
)
class GenerateTemplateView(APIView):  # Kept as APIView due to file download
    def get(self, request, session_id, course_id):
        try:
            session = AcademicSession.objects.get(academic_session_id=session_id)
            course = Course.objects.get(course_id=course_id)
        except (AcademicSession.DoesNotExist, Course.DoesNotExist):
            return Response({"error": "Invalid session or course"}, status=status.HTTP_400_BAD_REQUEST)

        wb = openpyxl.Workbook()
        ws = wb.active
        ws.title = f"{course.course_code} Scores"
        ws.append(["student_id", "course_code", "score"])
        ws.append(["", course.course_code, ""])

        response = HttpResponse(content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
        response["Content-Disposition"] = f"attachment; filename={course.course_code}_template.xlsx"
        wb.save(response)
        return response

@extend_schema_view(
    post=extend_schema(
        summary='Upload score sheet',
        description='Upload an Excel file with student scores for a session and course',
        tags=['Score Sheet Upload'],
        request={'multipart/form-data': {'file': 'file'}},
        responses={
            201: UploadResponseSerializer,
            400: UploadResponseSerializer
        }
    )
)
class UploadScoreSheetView(APIView):  # Kept as APIView due to custom file processing
    def post(self, request, session_id, course_id):
        file = request.FILES.get("file")
        if not file:
            return Response({"error": "No file uploaded"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            session = AcademicSession.objects.get(academic_session_id=session_id)
            course = Course.objects.get(course_id=course_id)
        except (AcademicSession.DoesNotExist, Course.DoesNotExist):
            return Response({"error": "Invalid session or course"}, status=status.HTTP_400_BAD_REQUEST)

        upload = UploadHistory.objects.create(
            session=session,
            course=course,
            uploaded_file=file,
            uploaded_by=request.user
        )

        wb = openpyxl.load_workbook(file)
        ws = wb.active
        errors = []
        for row in ws.iter_rows(min_row=2, values_only=True):
            student_id, course_code, score = row
            if not score:
                errors.append(f"Missing score for student {student_id}")
                continue

            try:
                session_reg = SessionRegistration.objects.get(
                    student__student_id=student_id,
                    session=session
                )
                CourseRegistration.objects.create(
                    session_registration=session_reg,
                    course=course,
                    score=score
                )
            except SessionRegistration.DoesNotExist:
                errors.append(f"Student {student_id} not registered for session {session}")
            except Exception as e:
                errors.append(str(e))

        upload.parse_status = ParseStatus.FAILED if errors else ParseStatus.SUCCESS
        upload.save()

        response_data = {
            "message": "Upload successful" if not errors else "Upload failed",
            "upload_id": upload.upload_history_id
        }
        if errors:
            response_data["errors"] = errors
            return Response(response_data, status=status.HTTP_400_BAD_REQUEST)
        return Response(response_data, status=status.HTTP_201_CREATED)

@extend_schema_view(
    get=extend_schema(
        summary='List upload history',
        description='Retrieve the history of all score sheet uploads',
        tags=['Score Sheet Upload'],
        responses={200: UploadHistorySerializer(many=True)}
    )
)
class UploadHistoryView(ListAPIView):
    queryset = UploadHistory.objects.all()
    serializer_class = UploadHistorySerializer