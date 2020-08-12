from django import forms

from match.models.reaction import Reaction


class ReactionForm(forms.Form):
    LIKE =  0
    reaction_users = Reaction()
    count = -1

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def load(self, user_id):
        # 自分にいいねをしてくれた人のuser_idを取得
        mylikeusers = self.__toFromIdsArray(Reaction.objects.filter(from_user_id=user_id, status=self.LIKE))
        # いいねをしてくれた人の中から自分がいいねをつけたユーザーを取得
        "→具体的にいうと、下記のコードでいいねを押してくれた人の中から自分がいいねをつけたリアクションのレコードを取得する"
        self.reaction_users = Reaction.objects.filter(to_user_id__in=mylikeusers, status=self.LIKE, from_user_id=user_id)
        self.count = len(self.reaction_users)

    def __toFromIdsArray(self, mylike_users):
        mylike_userids = list()
        for likeuser in mylike_users:
            mylike_userids.append(likeuser.to_user_id)
        return mylike_userids