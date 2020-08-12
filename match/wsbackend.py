from channels.generic.websocket import WebsocketConsumer
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from .controller import chat_controller
from django.shortcuts import render
import json


class WSBackend(WebsocketConsumer):
    """
    WebSocketでの通信をハンドルする
    """
    group_name = 'chat'
    channel_layer = get_channel_layer()

    def connect(self):
        async_to_sync(self.channel_layer.group_add)(
            self.group_name,
            self.channel_name
        )
        self.accept()

    def disconnect(self, close_code):
       async_to_sync(self.channel_layer.group_discard)(
           self.group_name,
           self.channel_name
       )
       pass

    def receive(self, text_data=None, bytes_data=None):
        """
        受け取ったメッセージを返却する
        """
        text_data_json = json.loads(text_data)
        username = text_data_json['username']
        message = text_data_json['message']
        room_id = int(text_data_json['room_id'])
        user_id = int(text_data_json['user_id'])
        chat_controller.registmessage(room_id, user_id, message)
        async_to_sync(self.channel_layer.group_send)(
            self.group_name,
            {
                'type': 'chat_message',
                'username': username,
                'message': message
            }
        )

    def chat_message(self, event):
        username = event['username']
        message = event['message']
        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'username': username,
            'message': message
        }))