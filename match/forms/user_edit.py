from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from match.models.image import Image

from match.models.userinfo import UserInfo


class EditForm(forms.Form):
    image = forms.ImageField()
    error_message = ''
    username = forms.CharField(label='LOGIN_ID', max_length=30,
        widget=forms.TextInput(
          attrs={'placeholder':'名前を入力してください', 'class':'form-contorol'}
        )
    )
    password = forms.CharField(label='PASSWORD', max_length=128,
        widget=forms.PasswordInput(
          attrs={'placeholder':'パスワードを入力してください', 'class':'form-contorol', 'autocomplete':'off'}
        )
    )
    SEX = [('man', '男'), ('woman', '女')]
    sex = forms.ChoiceField(choices=SEX, widget=forms.RadioSelect())
    self_introduction = forms.CharField(required=False, label='SELF_INTRODUCTION', max_length=1000,
        widget=forms.Textarea(
          attrs={'rows':10, 'class':'form-control'}
        )
    )
    info = UserInfo()
    is_save = False

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def load(self, userid):
        self.info = UserInfo.objects.get(pk=userid)

    def save(self, post, userid):
        user = User.objects.get(pk=userid)
        user.set_password(post['password'])
        user.save()

        image = Image.objects.get(pk=userid)
        image.origin = self.cleaned_data['image']
        image.save()

        info = UserInfo.objects.get(pk=userid)
        info.name = post['username']
        info.self_introduction = post['self_introduction']
        info.sex = post['sex']
        info.save()

        self.is_save = True