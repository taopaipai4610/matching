from django.db import models
from match.models.chatroom import ChatRoom
from match.models.userinfo import UserInfo


class ChatRoomUser(models.Model):
    chat_room = models.ForeignKey(ChatRoom, on_delete=models.CASCADE, related_name="roomuser_roomid")
    user = models.ForeignKey(UserInfo, on_delete=models.CASCADE, related_name="roomuser_userid")
    objects = models.Manager