from django.contrib.auth.models import User
from rest_framework import authentication, generics, mixins, permissions, status
from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes,
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from users.serializers import UserSerializer

# from rest_framework.views import APIView


# create user
class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# class NotificationCreate(APIView):
#     authentication_classes = [authentication.TokenAuthentication]


@api_view(["GET"])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_notification_view(request: Request, *args, **kwargs):
    print(request)
    print(kwargs)
    return Response({"hello": "world!"}, status=status.HTTP_200_OK)
