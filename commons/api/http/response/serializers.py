from django.utils import timezone
from rest_framework import serializers, status


class DefaultResponse:
    def __init__(self, status_code=status.HTTP_200_OK, message=None, data=None):
        self.status_code = status_code
        self.message = message
        self.data = data


class DefaultErrorResponseSerializer(serializers.Serializer):
    status_code = serializers.IntegerField()
    error_message = serializers.CharField(max_length=255)
    traceback = serializers.CharField(max_length=64)
    timestamp = serializers.DateTimeField(default=timezone.now)


class DefaultResponseSerializer(serializers.Serializer):
    status_code = serializers.IntegerField()
    message = serializers.CharField(max_length=255)
    data = serializers.DictField()
