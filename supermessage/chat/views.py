from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from slack_sdk import WebClient

from supermessage.settings import SLACK_URL


# Create your views here.
@api_view(["POST"])
def start_new_conversation_view(request: Request):
    return Response("start new chat view!")


@api_view(["GET"])
def get_conversation_details_view(request: Request, *args, **kwargs):
    return Response(f"Get chat details view! with chat_id of {kwargs['chat_id']}")


@api_view(["POST"])
def post_conversation_message_view(request: Request, *args, **kwargs):
    client = WebClient(token=SLACK_URL)
    text = request.data["text"]
    if not text:
        content = {"message": "please enter text in body"}
        return Response(content, status=status.HTTP_400_BAD_REQUEST)

    client.chat_postMessage(channel=kwargs["channel_id"].upper(), text=text)
    content = {"message": f"Succesfully sent message of: '{text}' to channel"}

    return Response(content, status=status.HTTP_200_OK)


@api_view(["GET"])
def get_conversation_messages_view(request: Request, *args, **kwargs):
    client = WebClient(token=SLACK_URL)
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


@api_view(["POST"])
def post_join_new_conversation(request: Request, *args, **kwargs):
    client = WebClient(token=SLACK_URL)
    response = client.conversations_join(channel=kwargs["channel_id"].upper())
    content = {"message": f"Joined '{response['channel']['name']}' channel"}

    return Response(content, status=status.HTTP_200_OK)


@api_view(["DELETE"])
def delete_conversation_message_view(request: Request, *args, **kwargs):
    client = WebClient(token=SLACK_URL)
    client.chat_delete(channel=kwargs["channel_id"].upper(), ts=request.data["ts"])
    content = {"message": "Message successfully deleted"}

    return Response(content, status=status.HTTP_200_OK)
