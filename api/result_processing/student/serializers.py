from rest_framework import serializers

from appdata.models import Student


class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = '__all__'
        read_only_fields = ('student_id', 'date_created',
                            'date_last_modified', 'created_by_user', 'last_modified_by_user')


class MinimalStudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        exclude = ('date_created', 'date_last_modified', 'created_by_user', 'last_modified_by_user')
        read_only_fields = ('student_id', )
