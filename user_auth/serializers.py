from rest_framework import serializers

from user_auth.models import Profile
from competitions.serializers import (
    SkillTokenSerializer)


class ProfileSerializer(serializers.ModelSerializer):
    skilltokens = SkillTokenSerializer(many=True)

    class Meta:
        model = Profile
        fields = ['email', 'role', 'username', 'skilltokens']
