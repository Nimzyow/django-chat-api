from rest_framework import authentication, status
from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes,
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from slack_sdk import WebClient

from supermessage.settings import SLACK_URL


def generate_slack_client():
    return WebClient(token=SLACK_URL)


@api_view(["POST"])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([IsAuthenticated])
def open_conversation_view(request: Request, *args, **kwargs):
    client = generate_slack_client()
    users = request.data["users"]

    response = client.conversations_open(users=users, return_im=True)
    channel_id = response.data["channel"]["id"]
    content = {"message": f"Succesfully opened channel with ID: '{channel_id}'"}

    return Response(content, status=status.HTTP_200_OK)


@api_view(["GET"])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_conversation_details_view(request: Request, *args, **kwargs):
    return Response(f"Get chat details view! with chat_id of {kwargs['chat_id']}")


@api_view(["POST"])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([IsAuthenticated])
def post_conversation_message_view(request: Request, *args, **kwargs):
    client = generate_slack_client()
    text = request.data["text"]
    if not text:
        content = {"message": "please enter text in body"}
        return Response(content, status=status.HTTP_400_BAD_REQUEST)

    client.chat_postMessage(channel=kwargs["channel_id"].upper(), text=text)
    content = {"message": f"Succesfully sent message of: '{text}' to channel"}

    return Response(content, status=status.HTTP_200_OK)


@api_view(["GET"])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_conversation_messages_view(request: Request, *args, **kwargs):
    client = generate_slack_client()
    response = client.conversations_history(channel=kwargs["channel_id"].upper())
    content = []
    for item in response.data["messages"]:
        content.append(
            {
                "user": item["user"],
                "text": item["text"],
                "ts": item["ts"],
            }
        )

    return Response(content, status=status.HTTP_200_OK)


@api_view(["DELETE"])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([IsAuthenticated])
def delete_conversation_message_view(request: Request, *args, **kwargs):
    client = generate_slack_client()
    client.chat_delete(channel=kwargs["channel_id"].upper(), ts=request.data["ts"])
    content = {"message": "Message successfully deleted"}

    return Response(content, status=status.HTTP_200_OK)
