from rest_framework import serializers

from appdata.models import Course


class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = '__all__'
        read_only_fields = ('course_id', 'date_created',
                            'date_last_modified', 'created_by_user', 'last_modified_by_user')
