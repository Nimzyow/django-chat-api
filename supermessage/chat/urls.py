from chat.views import chat_get_message_view
from django.urls import path

urlpatterns = [
    path("chat/1", chat_get_message_view, name="chat"),
]
