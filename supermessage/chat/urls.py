from chat.views import (
    delete_conversation_message_view,
    get_conversation_details_view,
    get_conversation_messages_view,
    open_conversation_view,
    post_conversation_message_view,
)
from django.urls import re_path

urlpatterns = [
    re_path(
        r"^chat/open$",
        open_conversation_view,
        name="open_channel",
    ),
    re_path(
        r"^chat/(?P<chat_id>[A-Za-z0-9]+)/$", get_conversation_details_view, name="get_chat_details"
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
        r"^chat/(?P<channel_id>[A-Za-z0-9]+)$",
        delete_conversation_message_view,
        name="delete_chat_message",
    ),
]
