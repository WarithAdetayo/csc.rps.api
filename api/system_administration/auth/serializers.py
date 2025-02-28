from api.system_administration.osafe_users.services import UserService
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class ObtainTokenPairSerializer(TokenObtainPairSerializer):

    def validate(self, attrs):
        username_or_email = attrs.get('email')
        password = attrs.get('password')

        user = UserService.get_user_by_email_or_username(username_or_email)
        if user is None or not user.check_password(password):
            raise serializers.ValidationError("Invalid credentials")

        attrs[self.username_field] = user.email
        return super().validate(attrs)
