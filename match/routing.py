from django.urls import path

from . import wsbackend

websocket_urlpatterns = [
    path('ws/chat/<str:room_name>/', wsbackend.WSBackend),
]