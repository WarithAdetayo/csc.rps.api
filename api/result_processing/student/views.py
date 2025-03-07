from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from api.result_processing.student.serializers import StudentSerializer
from appdata.models import Student


@extend_schema_view(
    get=extend_schema(summary='Retrieve all students',
                      description='Retrieve all students',
                      tags=['Students']),
    post=extend_schema(summary='Add new student',
                       description='Add new student',
                       tags=['Students'])
)
class StudentListCreateView(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


@extend_schema_view(
    get=extend_schema(summary='Retrieve student by id',
                      description='Retrieve student by id',
                      tags=['Students']),
    put=extend_schema(summary='Update student',
                      description='Update student',
                      tags=['Students']),
    patch=extend_schema(summary='Update student',
                        description='Update student',
                        tags=['Students']),
    delete=extend_schema(summary='Delete a student',
                         description='Delete a student',
                         tags=['Students']),
)
class StudentDetailView(RetrieveUpdateDestroyAPIView):
    lookup_field = 'student_id'
    serializer_class = StudentSerializer
    queryset = Student.objects.all()
