from rest_framework import serializers

from user_auth.models import Profile
from competitions.serializers import CompetencySerializer


class ProfileSerializer(serializers.ModelSerializer):
    competencies = CompetencySerializer(many=True, read_only=True)

    class Meta:
        model = Profile
        fields = ['email', 'role', 'username', 'competencies']
