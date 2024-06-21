from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from slack_sdk import WebClient

from supermessage.settings import SLACK_URL


# Create your views here.
@api_view(["POST"])
def start_new_chat_view(request: Request):
    return Response("start new chat view!")


@api_view(["GET"])
def get_chat_details_view(request: Request, *args, **kwargs):
    return Response(f"Get chat details view! with chat_id of {kwargs['chat_id']}")


@api_view(["POST"])
def post_message_view(request: Request, *args, **kwargs):
    return Response(
        f"Post a new message in a chat! with chat_id of {kwargs['chat_id']}"
    )


@api_view(["GET"])
def get_chat_messages_view(request: Request, *args, **kwargs):
    return Response(f"Get chat messagesss view! with chat_id of {kwargs['chat_id']}")


@api_view(["POST"])
def post_join_new_conversation(request: Request, *args, **kwargs):
    client = WebClient(token=SLACK_URL)
    response = client.conversations_join(channel=kwargs["channel_id"].upper())
    content = {"message": f"Joined '{response['channel']['name']}' channel"}

    return Response(content, status=status.HTTP_200_OK)


@api_view(["DELETE"])
def delete_chat_message_view(request: Request, *args, **kwargs):
    return Response(
        f"Delete chat message view! with chat_id of {kwargs['chat_id']}"
        + f" and a message_id of {kwargs['message_id']}"
    )
