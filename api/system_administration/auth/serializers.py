# from api.system_administration.osafe_users.services import UserService
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from api.system_administration.csc_rps_user.services import UserService


class ObtainTokenPairSerializer(TokenObtainPairSerializer):

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        user = UserService.get_user_by_email(email)
        if user is None or not user.check_password(password):
            raise serializers.ValidationError("Invalid credentials")

        attrs[self.username_field] = user.email
        return super().validate(attrs)
