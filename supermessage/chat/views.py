from django.http import HttpRequest, HttpResponse
from slack_sdk import WebClient

from supermessage.settings import SLACK_URL


# Create your views here.
def start_new_chat_view(request: HttpRequest):
    return HttpResponse("start new chat view!")


def get_chat_details_view(request: HttpRequest, *args, **kwargs):
    return HttpResponse(f"Get chat details view! with chat_id of {kwargs['chat_id']}")


def post_message_view(request: HttpRequest, *args, **kwargs):
    return HttpResponse(
        f"Post a new message in a chat! with chat_id of {kwargs['chat_id']}"
    )


def get_chat_messages_view(request: HttpRequest, *args, **kwargs):
    return HttpResponse(
        f"Get chat messagesss view! with chat_id of {kwargs['chat_id']}"
    )


def post_join_new_channel(request: HttpRequest, *args, **kwargs):
    client = WebClient(token=SLACK_URL)
    response = client.conversations_join(channel="C078F8L651V")
    print(response)
    return HttpResponse(
       "Joined channel"
    )


def delete_chat_message_view(request: HttpRequest, *args, **kwargs):
    return HttpResponse(
        f"Delete chat message view! with chat_id of {kwargs['chat_id']}"
        + f" and a message_id of {kwargs['message_id']}"
    )
