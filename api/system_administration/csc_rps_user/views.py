from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework.generics import CreateAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny

from api.system_administration.csc_rps_user.serializers import CreateAccountSerializer, ProfilePictureSerializer


@extend_schema_view(
    post=extend_schema(summary='Create an account',
                       description='Create an account',
                       tags=['User'])
)
class CreateAccountAPIView(CreateAPIView):
    serializer_class = CreateAccountSerializer
    permission_classes = [AllowAny]


@extend_schema_view(
    put=extend_schema(summary='Upload user account profile picture',
                      description='Upload user account profile picture',
                      tags=['User'],
                      request={
                          'multipart/form-data': {
                              'type': 'object',
                              'properties': {
                                  'profile_picture': {
                                      'type': 'string',
                                      'format': 'binary'
                                  }
                              }
                          }
                      })
)
class ChangeProfilePictureAPIView(UpdateAPIView):
    serializer_class = ProfilePictureSerializer
    permission_classes = (IsAuthenticated,)
    allowed_methods = ('PUT', )

    def get_object(self):
        return self.request.user
