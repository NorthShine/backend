from rest_framework import serializers

from competitions.models import Competency, CompetencyLevel
from user_auth.models import Profile


class CompetencyLevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompetencyLevel
        fields = ['name']


class CompetencyProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['email']


class CompetencySerializer(serializers.ModelSerializer):
    level = CompetencyLevelSerializer()
    user = CompetencyProfileSerializer()

    def create(self, validated_data):
        level_info = validated_data.pop('level')
        user = validated_data.pop('user')
        level = CompetencyLevel.objects.get(name=level_info['name'])
        user = Profile.objects.get(email=user['email'])
        competency = Competency.objects.create(
            name=validated_data['name'],
            level=level,
            user=user
        )
        return competency

    class Meta:
        model = Competency
        depth = 1
        fields = ['name', 'level', 'user']
