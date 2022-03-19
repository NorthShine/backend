from rest_framework import serializers

from user_auth.models import Profile
from competitions.models import Competency
from competitions.serializers import CompetencySerializer


class CompetencySerializerWithID(CompetencySerializer):
    class Meta:
        model = Competency
        depth = 1
        fields = ['name', 'level', 'user', 'id']


class ProfileSerializer(serializers.ModelSerializer):
    competencies = CompetencySerializerWithID(many=True, read_only=True)

    class Meta:
        model = Profile
        fields = ['email', 'role', 'username', 'competencies']
