from rest_framework import serializers

from api.result_processing.academic_session.serializers import MinimalAcademicSessionSerializer
from api.result_processing.level.serializers import MinimalLevelSerializer
from api.result_processing.student.serializers import MinimalStudentSerializer
from appdata.models import SessionRegistration, Student, AcademicSession, Level


class SessionRegistrationSerializer(serializers.ModelSerializer):
    student = MinimalStudentSerializer(read_only=True)
    session = MinimalAcademicSessionSerializer(read_only=True)
    level = MinimalLevelSerializer(read_only=True)

    student_id = serializers.CharField(write_only=True, required=True)
    session_id = serializers.CharField(write_only=True, required=True)
    level_id = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = SessionRegistration
        fields = '__all__'
        read_only_fields = ('session_registration_id', 'date_created',
                            'date_last_modified', 'created_by_user', 'last_modified_by_user')

    def validate(self, data):
        """
        Validate and replace IDs with actual related objects.
        """
        errors = {}

        # Validate student_id
        student_id = data.pop('student_id', None)
        if student_id:
            try:
                data['student'] = Student.objects.get(pk=student_id)
            except Student.DoesNotExist:
                errors['student_id'] = 'Invalid student ID'

        # Validate session_id
        session_id = data.pop('session_id', None)
        if session_id:
            try:
                data['session'] = AcademicSession.objects.get(pk=session_id)
            except AcademicSession.DoesNotExist:
                errors['session_id'] = 'Invalid session ID'

        # Validate level_id
        level_id = data.pop('level_id', None)
        if level_id:
            try:
                data['level'] = Level.objects.get(pk=level_id)
            except Level.DoesNotExist:
                errors['level_id'] = 'Invalid level ID'

        # If there are validation errors, raise an exception
        if errors:
            raise serializers.ValidationError(errors)

        return data
