from rest_framework.views import APIView
from rest_framework.response import Response

from competitions.models import CompetencyLevel, Competency, SkillToken
from competitions.serializers import (
    CompetencyLevelSerializer,
    CompetencySerializer,
    SkillTokenSerializer)
from competitions.search import search
from user_auth.models import Profile


class CreateCompetitionLevel(APIView):
    def post(self, request):
        data = request.data
        instance = CompetencyLevelSerializer(data=data)
        instance.is_valid()
        instance.save()

        obj = CompetencyLevel.objects.get(name=data['name'])
        return Response(data={'id': obj.id, 'name': obj.name})

    def delete(self, request):
        data = request.data
        instance = CompetencyLevelSerializer(data=data)
        instance.is_valid()

        CompetencyLevel.objects.filter(name=data['name']).delete()
        return Response(data={'response': f'Deleted {instance["name"]}'})


class CreateCompetency(APIView):
    def post(self, request):
        data = request.data
        instance = CompetencySerializer(data=data)
        instance = instance.create(instance.initial_data)

        response = CompetencySerializer(instance=instance)
        return Response(data=response.data)

    def delete(self, request):
        data = request.data
        competency_id = data['id']

        Competency.objects.filter(id=competency_id).delete()
        return Response(
            data={
                'response': f'deleted competency with id {competency_id}'})


class SkillTokenView(APIView):
    def post(self, request):
        data = request.data
        instance = SkillTokenSerializer(data=data)
        instance.create(data)
        return Response(data=data)

    def get(self, request, email):
        profile = Profile.objects.get(email=email)
        skill_token = SkillToken.objects.filter(profile=profile)
        serialized = SkillTokenSerializer(skill_token, many=True)
        serialized = serialized.data
        return Response(data=serialized)

    def delete(self, request, id):
        skilltoken = SkillToken.objects.filter(id=id).delete()
        return Response(f'Deleted {skilltoken} objects with id: {id}')


class SkillTokenSearchView(APIView):
    def get(self, request):
        query = request.GET.get('q')
        results = search(query)
        serialized = SkillTokenSerializer(results, many=True)
        serialized = serialized.data
        return Response(data=serialized)
