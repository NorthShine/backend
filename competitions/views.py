import json
import hashlib

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework_simplejwt.authentication import JWTAuthentication

from competitions.models import CompetencyLevel
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


class CreateCompetency(APIView):
    def post(self, request):
        data = request.data
        instance = CompetencySerializer(data=data)
        instance = instance.create(instance.initial_data)

        response = CompetencySerializer(instance=instance)
        return Response(data=response.data)
