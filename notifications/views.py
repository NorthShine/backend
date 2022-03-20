from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.cache import cache

from user_auth.models import Profile
from notifications.logic import get_messages_for_recipient, send_message


class RedisNotification(APIView):
    def get(self, request, recipient_id):
        messages = cache.get(recipient_id)
        return Response(data={"message": messages})

    def post(self, request):
        data = request.data
        recipient = data.get('recipient_id')
        email = recipient.split(':')[0]
        profile = Profile.objects.filter(email=email)
        if not profile.exists():
            return Response(
                data={'error': f'Profile with email {recipient} was not found'},
                status=404)
        message = data.get('message')
        cache.set(recipient, message)
        return Response(data={'msg': f'Message to {recipient} is sent'})


class PersistentNotificationView(APIView):
    def get(self, request, recipient_id):
        messages = get_messages_for_recipient(recipient_id)
        return Response(data=messages)
