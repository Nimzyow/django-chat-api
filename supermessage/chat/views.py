from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


# Create your views here.
def start_new_chat_view(request: HttpRequest):
    return HttpResponse("start new chat view")


def get_chat_details_view(request: HttpRequest):
    return HttpResponse("Get chat details view")


def post_message_view(request: HttpRequest):
    return HttpResponse("Post a new message in a chat!")


def get_chat_messages_view(request: HttpRequest):
    return HttpResponse("Get chat messagesss view!")


def delete_chat_message_view(request: HttpRequest):
    return HttpResponse("Delete chat message view!")
