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

    class Meta:
        model = Competency
        fields = ['name', 'level', 'user']
