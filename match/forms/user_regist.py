from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from match.models.userinfo import UserInfo
from match.models.image import Image

User = get_user_model()

# 登録フォーム
class RegistForm(UserCreationForm):
    image = forms.ImageField()
    error_message = ''
    username = forms.CharField(label='LOGIN_ID', max_length=30,
        # widgetはHTMLのレンダリングとこれに対応するGET/POSTオブジェクトからデータを取り出す
        widget=forms.TextInput(
        attrs={'placeholder':'名前を入力してください', 'class':'form-control'}))
    email = forms.CharField(label='EMAIL', max_length=30,
        widget=forms.TextInput(
        attrs={'placeholder':'emailを入力してください', 'class':'form-control', 'autocomplete': 'email'}))
    password1 = forms.CharField(
        label='PASSWORD', max_length=128,
        widget=forms.PasswordInput(
        attrs={'placeholder':'パスワードを入力してください', 'class':'form-control', 'autocomplete' : 'off'}))
    password2 = forms.CharField(
        label='PASSWORDCONFIRM', max_length=128,
        widget=forms.PasswordInput(
        attrs={'placeholder':'パスワードを再度入力してください', 'class':'form-control', 'autocomplete' : 'off'}))
    SEX=[('man','男'),
        ('woman','女')]
    sex = forms.ChoiceField(choices=SEX, widget=forms.RadioSelect())
    self_introduction = forms.CharField(required=False, label='SELF_INTRODUCTION', max_length=1000,
        widget=forms.Textarea(
        attrs={'rows' : 10, 'class':'form-control'}))
    is_save = False

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def save(self, post):
        # UserCreationFormのクラスの保存処理を呼び出す
        user = super().save()
        # Imageインスタンスの作成
        image = Image()
        # 実際の画像データとユーザー情報を紐づけるためのidをセット
        image.id = user.id
        image.origin = self.cleaned_data['image'] # バリデート後のデータを型に応じて一定のやり方で整形して返す
        image.save()

        # UserInfoインスタンスを生成し、必要情報をセット
        info = UserInfo()
        info.id = user.id
        info.image = image
        info.name = post['username']
        info.self_introduction = post['self_introduction']
        info.sex = post['sex']
        info.save()

        # メンバ変数の更新を実施
        # ＝外からこのフォームが保存を完了したかを判断するためのフラグ
        self.is_save = True