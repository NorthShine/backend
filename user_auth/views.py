import json
import hashlib

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework_simplejwt.authentication import JWTAuthentication

from user_auth.models import Profile
from user_auth.serializers import ProfileSerializer


class ListProfile(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.AllowAny]

    def get(self, request, email):
        user = Profile.objects.filter(email=email)
        if not user.exists():
            return Response(data=f'user with email {email} not found')
        user = user.first()
        data = ProfileSerializer(instance=user)
        serialized = data.data
        return Response(data=serialized)


class CreateUser(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        data = request.data
        email = data['email']
        role = data['role']
        username = hashlib.md5(email.encode())
        user = Profile.objects.create_user(
            email=email,
            username=username,
            password='dummypassword',
            role=role)
        return Response(
            data={
                'username': str(user.username.digest()),
                'email': user.email,
                'role': user.role
                })
