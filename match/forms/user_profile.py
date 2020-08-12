from django import forms
from match.models.userinfo import UserInfo
from match.models.image import Image

# 新規登録画面で登録したユーザー情報を表示するためにform情報とuser情報を取得してテンプレートで表示できるようにする
class ProfileForm(forms.Form):
    info = UserInfo()
    image = Image()

    def __init__(self, *args, **kwargs):
        # 親クラスのコンストラクタを継承
        super().__init__(*args, **kwargs)

    def load(self, userid):
        self.info = UserInfo.objects.get(pk=userid)
        self.image = Image.objects.get(pk=userid)