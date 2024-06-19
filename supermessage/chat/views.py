from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


# Create your views here.
def chat_get_message_view(request: HttpRequest):
    return HttpResponse("Hello, World!")
