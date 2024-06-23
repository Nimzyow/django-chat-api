import json

from django.contrib.auth.models import User
from django.core import serializers
from rest_framework import authentication, generics, mixins, permissions, status
from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes,
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from users.models import Notification
from users.serializers import UserSerializer

# from rest_framework.views import APIView

class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


@api_view(["GET", "PUT"])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([IsAuthenticated])
def notification_view(request: Request, *args, **kwargs):
    if request.method == "GET":
        notification_instance = Notification(user=request.user)
        serialized_obj = serializers.serialize(
            "json",
            [
                notification_instance,
            ],
        )
        content = {"body": {"notification": serialized_obj}}

        return Response(content, status=status.HTTP_200_OK)
    if request.method == "PUT":
        notification_instance = Notification(
            user=request.user, notification_option=request.data["notification_option"]
        )
        notification_instance.save()
        serialized_obj = serializers.serialize(
            "json",
            [
                notification_instance,
            ],
        )
        content = {"body": {"notification": serialized_obj}}

        return Response(content, status=status.HTTP_200_OK)
