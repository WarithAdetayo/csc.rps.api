from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from api.result_processing.academic_session.serializers import AcademicSessionSerializer
from api.result_processing.course.serializers import CourseSerializer
from appdata.models import AcademicSession, Course


@extend_schema_view(
    get=extend_schema(summary='Retrieve all courses',
                      description='Retrieve all course',
                      tags=['Department Courses']),
    post=extend_schema(summary='Add new course',
                       description='Add new course',
                       tags=['Department Courses'])
)
class CourseListCreateView(ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


@extend_schema_view(
    get=extend_schema(summary='Retrieve course by id',
                      description='Retrieve course by id',
                      tags=['Department Courses']),
    put=extend_schema(summary='Update course',
                      description='Update course',
                      tags=['Department Courses']),
    patch=extend_schema(summary='Update course',
                        description='Update course',
                        tags=['Department Courses']),
    delete=extend_schema(summary='Delete a course',
                         description='Delete a course',
                         tags=['Department Courses']),
)
class CourseDetailView(RetrieveUpdateDestroyAPIView):
    lookup_field = 'course_id'
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
