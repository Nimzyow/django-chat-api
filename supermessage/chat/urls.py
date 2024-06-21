from chat.views import (
    delete_chat_message_view,
    get_chat_details_view,
    get_chat_messages_view,
    post_join_new_conversation,
    post_message_view,
    start_new_chat_view,
)
from django.urls import re_path

urlpatterns = [
    re_path("^chat/$", start_new_chat_view, name="start_new_chat"),
    re_path(
        r"^chat/(?P<chat_id>\d+)/$", get_chat_details_view, name="get_chat_details"
    ),
    re_path(
        r"^chat/(?P<chat_id>\d+)/messages/$",
        get_chat_messages_view,
        name="get_chat_messages",
    ),
    re_path(
        r"^chat/(?P<chat_id>\d+)/message/$", post_message_view, name="post_chat_message"
    ),
    re_path(
        r"^chat/(?P<chat_id>\d+)/messages/(?P<message_id>\d+)/$",
        delete_chat_message_view,
        name="delete_chat_message",
    ),
    re_path(
        r"^join/(?P<channel_id>[A-Za-z0-9]+)$",
        post_join_new_conversation,
        name="join_new_channel",
    ),
]
