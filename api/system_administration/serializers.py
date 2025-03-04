from rest_framework import serializers
from appdata.models import UploadHistory, Course, AcademicSession

class UploadHistorySerializer(serializers.ModelSerializer):
    session = serializers.CharField(source='session.session')  # Nested field from AcademicSession
    course = serializers.CharField(source='course.course_code')  # Nested field from Course

    class Meta:
        model = UploadHistory
        fields = ['upload_history_id', 'session', 'course', 'upload_timestamp', 'parse_status']

class UploadResponseSerializer(serializers.Serializer):
    message = serializers.CharField()
    upload_id = serializers.CharField()
    errors = serializers.ListField(child=serializers.CharField(), required=False)