from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse
import openpyxl
from appdata.models import CourseRegistration, Course, UploadHistory, SessionRegistration, AcademicSession
from appdata.models.enums.choices import ParseStatus

class GenerateTemplateView(APIView):
    def get(self, request, session_id, course_id):
        try:
            session = AcademicSession.objects.get(academic_session_id=session_id)  # Fixed from id
            course = Course.objects.get(course_id=course_id)               # Fixed from id
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

class UploadScoreSheetView(APIView):
    def post(self, request, session_id, course_id):
        file = request.FILES.get("file")
        if not file:
            return Response({"error": "No file uploaded"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            session = AcademicSession.objects.get(academic_session_id=session_id)  # Fixed from id
            course = Course.objects.get(course_id=course_id)               # Fixed from id
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

        if errors:
            return Response({"errors": errors}, status=status.HTTP_400_BAD_REQUEST)
        return Response({"message": "Upload successful", "upload_id": upload.upload_history_id}, status=status.HTTP_201_CREATED)

class UploadHistoryView(APIView):
    def get(self, request):
        uploads = UploadHistory.objects.all().values(
            "upload_history_id",
            "session__session",
            "course__course_code",
            "upload_timestamp",
            "parse_status"
        )
        return Response(list(uploads))