from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework.authentication import SessionAuthentication
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from api.result_processing.level.serializers import LevelSerializer
from appdata.models import Level


@extend_schema_view(
    get=extend_schema(summary='Retrieve all Department levels',
                      description='Retrieve all department levels',
                      tags=['Department Levels']),
    post=extend_schema(summary='Add new level',
                       description='Add new Academic Session',
                       tags=['Department Levels'])
)
class LevelListCreateView(ListCreateAPIView):
    queryset = Level.objects.all()
    serializer_class = LevelSerializer


@extend_schema_view(
    get=extend_schema(summary='Retrieve Department Level by id',
                      description='Retrieve Level by id',
                      tags=['Department Levels']),
    put=extend_schema(summary='Update level',
                      description='Update level',
                      tags=['Academic Data']),
    patch=extend_schema(summary='Update level',
                        description='Update level',
                        tags=['Department Levels']),
    delete=extend_schema(summary='Delete a level',
                         description='Delete a level',
                         tags=['Department Levels']),
)
class LevelDetailView(RetrieveUpdateDestroyAPIView):
    lookup_field = 'level_id'
    serializer_class = LevelSerializer
    queryset = Level.objects.all()
    permission_classes = []
