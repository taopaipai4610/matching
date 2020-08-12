from django import forms

from match.models.userinfo import UserInfo

class UserListForm(forms.Form):
    # ユーザーリストフォーム

    exclude_userlist = UserInfo()
    list_length = -1
    currentuser_id = -1

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def load(self, user_id):
        self.currentuser_id = user_id
        self.exclude_userlist = UserInfo.objects.exclude(pk=self.currentuser_id)
        self.list_length = len(self.exclude_userlist)


# ユーザーリストフォーム
class UserListForm(forms.Form):
    # ユーザーのリストを取り除く
    exclude_userlist = UserInfo()
    list_length = -1
    currentuser_id = -1

    def __init__(self, *args, **kwargs):
      super().__init__(*args, **kwargs)

    def load(self, user_id):
      self.currentuser_id = user_id
      # 現在ログインしているユーザー以外のレコード全てをexclude_userlistに代入
      self.exclude_userlist = UserInfo.objects.exclude(pk=self.currentuser_id)
      self.list_length = len(self.exclude_userlist)