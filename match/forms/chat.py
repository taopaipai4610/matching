from django import forms
from django.db.models import Q

from match.models.chatroom import ChatRoom
from match.models.chatroomuser import ChatRoomUser
from match.models.chatmessage import ChatMessage
from match.models.userinfo import UserInfo


class ChatForm(forms.Form):
    room = ChatRoom()
    roomuser = ChatRoomUser()
    message = ""
    current_user_name = ""
    room_id = -1

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def load(self, user_id, room_id):
        self.room = ChatRoom.objects.get(pk=room_id)
        self.roomuser = ChatRoomUser.objects.get(Q(chat_room=self.room), ~Q(user=UserInfo.objects.get(pk=user_id)))
        self.room_id = self.room.id
        self.current_user_name = UserInfo.objects.get(pk=user_id).name