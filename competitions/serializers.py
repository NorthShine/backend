from rest_framework import serializers
from django.db.transaction import atomic

from competitions.models import Competency, CompetencyLevel, SkillTag, SkillToken
from user_auth.models import Profile


@atomic
def create_competencies(serializer, competencies_data):
    instances = []
    for competency in competencies_data:
        instance = serializer.create(competency)
        instances.append(instance)

    return instances


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

    @atomic
    def create(self, validated_data):
        level_info = validated_data.pop('level')
        user = validated_data.pop('user')
        skilltoken_id = validated_data.pop('skilltoken_id')
        level = CompetencyLevel.objects.get(name=level_info['name'])
        user = Profile.objects.get(email=user['email'])
        skilltoken = SkillToken.objects.get(id=skilltoken_id)
        competency = Competency.objects.create(
            name=validated_data['name'],
            level=level,
            user=user,
            skilltoken=skilltoken
        )
        return competency

    class Meta:
        model = Competency
        fields = ['name', 'level', 'user']


class SkillTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = SkillTag
        fields = ('name',)


class SkillTokenSerializer(serializers.ModelSerializer):
    tags = SkillTagSerializer(many=True)
    competencies = CompetencySerializer(many=True)

    @atomic
    def create(self, validated_data):
        name = validated_data.pop('name')
        tags = validated_data.pop('tags')
        ext_id = validated_data.pop('ext_id')
        user_email = validated_data.pop('user_email')

        existing_tags = SkillTag.objects.filter(name__in=tags)\
            .values_list('id', flat=True)
        tags_to_create = list(filter(lambda x: x not in existing_tags, tags))
        user = Profile.objects.get(email=user_email)

        skill_token = SkillToken.objects.create(
            name=name, profile=user, ext_id=ext_id)

        competencies = validated_data.pop('competencies')
        for competency in competencies:
            competency['skilltoken_id'] = skill_token.id
        competencies_serializer = CompetencySerializer()
        create_competencies(competencies_serializer, competencies)

        for name in tags_to_create:
            tag, _ = SkillTag.objects.get_or_create(name=name)
            skill_token.tags.add(tag)

        if existing_tags.exists():
            skill_token.tags.add(*list(existing_tags))

        skill_token.save()

        return skill_token

    class Meta:
        model = SkillToken
        fields = ('id', 'name', 'tags', 'competencies', 'ext_id')
