from rest_framework import serializers

from appdata.models import Level


class LevelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Level
        fields = '__all__'
        read_only_fields = ('level_id', 'date_created',
                            'date_last_modified', 'created_by_user', 'last_modified_by')
