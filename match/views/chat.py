from django.shortcuts import render, loader, redirect
from django.http import HttpResponse

from match.controller import chat_controller
from match.forms.chat import ChatForm
import json


def create(request, user_id):
    roomid = chat_controller.create(request.user.id, user_id)
    return redirect('/chat/show/' + str(roomid))

def show(request, room_id):
    form = ChatForm(request.GET)
    form.load(request.user.id, room_id)
    context = {
        'form':form
    }
    template = loader.get_template('chat.html')
    return HttpResponse(template.render(context, request))

def messages(request, room_id):
    context = chat_controller.messages(room_id)
    context_json = json.dumps(context)
    return HttpResponse(context_json)