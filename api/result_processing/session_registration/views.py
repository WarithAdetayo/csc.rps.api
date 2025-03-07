from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from api.result_processing.session_registration.serializers import SessionRegistrationSerializer
from appdata.models import SessionRegistration


@extend_schema_view(
    get=extend_schema(summary='Retrieve all session registrations',
                      description='Retrieve all session registration',
                      tags=['Session Registrations']),
    post=extend_schema(summary='Add new session registration',
                       description='Add new student',
                       tags=['Session Registrations'])
)
class SessionRegistrationListCreateView(ListCreateAPIView):
    queryset = SessionRegistration.objects.all()
    serializer_class = SessionRegistrationSerializer


@extend_schema_view(
    get=extend_schema(summary='Retrieve session registration by id',
                      description='Retrieve session registration by id',
                      tags=['Session Registrations']),
    put=extend_schema(summary='Update session registration',
                      description='Update session registration',
                      tags=['Session Registrations']),
    patch=extend_schema(summary='Update session registration',
                        description='Update session registration',
                        tags=['Session Registrations']),
    delete=extend_schema(summary='Delete a session registration',
                         description='Delete a session registration',
                         tags=['Session Registrations']),
)
class SessionRegistrationDetailView(RetrieveUpdateDestroyAPIView):
    lookup_field = 'session_registration_id'
    serializer_class = SessionRegistrationSerializer
    queryset = SessionRegistration.objects.all()
