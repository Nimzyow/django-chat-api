from chat.views import (
    delete_chat_message_view,
    get_chat_details_view,
    get_chat_messages_view,
    post_message_view,
    start_new_chat_view,
)
from django.urls import path

urlpatterns = [
    path("chat", start_new_chat_view, name="chat"),
    path("chat/1", get_chat_details_view, name="chat"),
    path("chat/1/message", post_message_view, name="chat"),
    path("chat/1/messages", get_chat_messages_view, name="chat"),
    path("chat/1/messages/3", delete_chat_message_view, name="chat"),
]
