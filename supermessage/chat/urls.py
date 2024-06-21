from chat.views import (
    delete_conversation_message_view,
    get_conversation_details_view,
    get_conversation_messages_view,
    post_conversation_message_view,
    post_join_new_conversation,
    start_new_conversation_view,
)
from django.urls import re_path

urlpatterns = [
    re_path("^chat/$", start_new_conversation_view, name="start_new_chat"),
    re_path(
        r"^chat/(?P<chat_id>\d+)/$", get_conversation_details_view, name="get_chat_details"
    ),
    re_path(
        r"^chat/(?P<channel_id>[A-Za-z0-9]+)/messages$",
        get_conversation_messages_view,
        name="get_chat_messages",
    ),
    re_path(
        r"^chat/(?P<channel_id>[A-Za-z0-9]+)/message$",
        post_conversation_message_view,
        name="post_chat_message",
    ),
    re_path(
        r"^chat/(?P<chat_id>\d+)/messages/(?P<message_id>\d+)/$",
        delete_conversation_message_view,
        name="delete_chat_message",
    ),
    re_path(
        r"^join/(?P<channel_id>[A-Za-z0-9]+)$",
        post_join_new_conversation,
        name="join_new_channel",
    ),
]
