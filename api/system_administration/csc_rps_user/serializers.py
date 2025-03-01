from rest_framework import serializers

from api.system_administration.csc_rps_user.services import UserService
from appdata.models import CSCRPSUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CSCRPSUser
        exclude = ('password', )
        read_only_fields = ('user_id', 'date_joined')


class CreateAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = CSCRPSUser
        fields = ('email', 'password', 'user_id', 'date_joined', 'is_verified',
                  'is_active', 'profile_picture', 'first_name', 'last_name')
        read_only_fields = ('user_id', 'date_joined', 'is_verified', 'is_active', 'profile_picture')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'min_length': 5,
                'style': {'input_type': 'password'},
                'trim_whitespace': False
            },
        }

    def create(self, validated_data):
        return UserService.create_user(validated_data=validated_data)


class ChangePasswordSerializer(serializers.ModelSerializer):
    old_password = serializers.CharField(required=True, write_only=True)
    new_password = serializers.CharField(required=True, write_only=True)

    class Meta:
        model = CSCRPSUser
        fields = ('email', 'password')

    def validate(self, data):
        old_password = data.pop('old_password')
        user = self.context.get('user')

        if not user.check_password(old_password):
            raise serializers.ValidationError({'old_password': "Incorrect old password."})

        return super().validate(data)

    def update(self, instance, validated_data):
        new_password = validated_data.pop('new_password')
        instance.set_password(new_password)
        instance.save()
        return instance


class ResetPasswordEmailSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)


class CompletePasswordResetSerializer(serializers.Serializer):
    token = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)


class ProfilePictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = CSCRPSUser
        fields = ('profile_picture', )
        extra_kwargs = {'profile_picture': {'required': True, 'allow_empty_file': False}}

    def update(self, instance, validated_data):
        return UserService.update_profile_picture(
            instance, validated_data.get('profile_picture', instance.profile_picture))
