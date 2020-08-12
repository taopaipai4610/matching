from django.db import models
from match.models.chatroom import ChatRoom
from match.models.userinfo import UserInfo


class ChatMessage(models.Model):
    chat_room = models.ForeignKey(ChatRoom, on_delete=models.CASCADE, related_name="message_roomid")
    user = models.ForeignKey(UserInfo, on_delete=models.CASCADE, related_name="message_userid")
    objects = models.Manager