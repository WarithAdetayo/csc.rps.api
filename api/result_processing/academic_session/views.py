from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from api.result_processing.academic_session.serializers import AcademicSessionSerializer
from appdata.models import AcademicSession


@extend_schema_view(
    get=extend_schema(summary='Retrieve all Academic sessions',
                      description='Retrieve all Academic Sessions',
                      tags=['Academic Data']),
    post=extend_schema(summary='Add new session',
                       description='Add new Academic Session',
                       tags=['Academic Data'])
)
class AcademicSessionListCreateView(ListCreateAPIView):
    queryset = AcademicSession.objects.all()
    serializer_class = AcademicSessionSerializer


@extend_schema_view(
    get=extend_schema(summary='Retrieve Academic session by id',
                      description='Retrieve Academic Session by id',
                      tags=['Academic Session']),
    put=extend_schema(summary='Update Academic Session',
                      description='Update Academic Session',
                      tags=['Academic Session']),
    patch=extend_schema(summary='Update Academic Session',
                        description='Update Academic Session',
                        tags=['Academic Data']),
    delete=extend_schema(summary='Delete a session',
                         description='Delete a session',
                         tags=['Academic Session']),
)
class AcademicSessionDetailView(RetrieveUpdateDestroyAPIView):
    lookup_field = 'academic_session_id'
    serializer_class = AcademicSessionSerializer
    queryset = AcademicSession.objects.all()
