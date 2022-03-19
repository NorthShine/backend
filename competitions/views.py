from rest_framework.views import APIView
from rest_framework.response import Response

from competitions.models import CompetencyLevel, Competency
from competitions.serializers import (
    CompetencyLevelSerializer,
    CompetencySerializer)


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
