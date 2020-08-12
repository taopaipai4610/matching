from django.urls import path
from .views import index, user, reaction, chat
from django.conf import settings
from django.conf.urls.static import static
from .controller import reaction_controller, chat_controller

app_name = 'match'

urlpatterns = [
    path('', index.top, name='index'),
    path('login/', index.Login.as_view(), name='login'),
    path('logout/', index.Logout.as_view(), name='logout'),
    path('users/', user.gets, name='users'),
    path('users/regist/', user.regist, name='regist'),
    path('users/profile/<int:user_id>', user.profile),
    path('users/<int:user_id>/edit/', user.edit),
    path('reactions/', reaction_controller.create, name='reactions'),
    path('matching/', reaction.matching, name='matching'),
    path('chat/create/<int:user_id>', chat.create, name='chat_create'),
    path('chat/show/<int:room_id>', chat.show, name='chat_show'),
    path('chat/create/<int:room_id>/messages/', chat.messages, name='chat_messages'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)