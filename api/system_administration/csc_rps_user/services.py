from typing import Any

from django.core.files.uploadedfile import InMemoryUploadedFile
from django.db.models import Q, QuerySet

from appdata.models import CSCRPSUser


class UserService:

    @classmethod
    def create_user(cls, validated_data: dict[str, Any]) -> CSCRPSUser:
        return CSCRPSUser.objects.create_user(**validated_data)

    @classmethod
    def get_user_by_email(cls, email: str) -> CSCRPSUser:
        return CSCRPSUser.objects.get(Q(email=email))

    @classmethod
    def get_user_queryset(cls) -> QuerySet[CSCRPSUser]:
        return CSCRPSUser.objects.all()

    @classmethod
    def update_profile_picture(cls, instance: CSCRPSUser, profile_picture: InMemoryUploadedFile) -> CSCRPSUser:
        # Delete previous profile image if it exists
        previous_image = instance.profile_picture
        if previous_image:
            previous_image.delete(save=False)  # Don't save to database yet

        # Update profile image
        instance.profile_picture = profile_picture
        instance.save()

        return instance

