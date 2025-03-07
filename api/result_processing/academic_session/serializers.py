from rest_framework import serializers

from appdata.models import AcademicSession


class AcademicSessionSerializer(serializers.ModelSerializer):

    class Meta:
        model = AcademicSession
        fields = '__all__'
        read_only_fields = ('academic_session_id', 'date_created',
                            'date_last_modified', 'created_by_user', 'last_modified_by_user')


class MinimalAcademicSessionSerializer(serializers.ModelSerializer):

    class Meta:
        model = AcademicSession
        fields = ('academic_session_id', 'session')
        read_only_fields = ('academic_session_id', )
