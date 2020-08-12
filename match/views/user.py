from django.shortcuts import render, loader, redirect
from django.http import HttpResponse

from match.forms.user_regist import RegistForm
from match.forms.user_profile import ProfileForm
from match.forms.user_edit import EditForm
from match.forms.user_list import UserListForm


def regist(request):
    if request.method == 'GET':
        form = RegistForm()
    else:
        form = RegistForm(request.POST, request.FILES)
        if form.is_valid():
            print('user_regist is_valid')
            form.save(request.POST)
            return redirect('/login/')
        else:
            print('user_regist false is_valid')

    template = loader.get_template('regist.html')
    context = {
        'form': form,
    }
    return HttpResponse(template.render(context, request))


# スワイプ画面
def gets(request):
    current_userid = request.user.id
    if request.method == 'GET':
        form = UserListForm(request.GET or None)
        form.load(current_userid)

    template = loader.get_template('users.html')
    context = {
        'form': form,
    }
    return HttpResponse(template.render(context, request))

# プロフィール画面
def profile(request, user_id):
    if request.method == 'GET':
      form = ProfileForm(request.GET or None)
      form.load(user_id)
      data = {
        'form': form,
        'iscurrent': request.user.id == user_id,
      }
      return render(request, 'profile.html', data)

# 編集機能
def edit(request, user_id):
    if request.method == 'GET':
        form = EditForm(request.GET or None)
        form.load(user_id)
    else:
        form = EditForm(request.POST or None, request.FILES)
        if form.is_valid():
            print('user_edit is_valid')
            form.save(request.POST, user_id)
        else:
            print('user_edit false is_valid')
        if form.is_save:
            return redirect('/users/profile/' + str(user_id))

    template = loader.get_template('edit.html')
    context = {
      'form': form,
    }
    return HttpResponse(template.render(context, request))