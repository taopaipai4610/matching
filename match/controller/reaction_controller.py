# ユーザーのリアクションをサーバーに伝えるコントローラー
# サーバーのAPIとしてリアクションを行なうという機能

from match.models.reaction import Reaction
from match.models.userinfo import UserInfo


def create(request):
    fromuser_id = request.user.id
    post = request.POST
    user_id = post["user_id"]
    reaction_status = post["reaction"]
    reactions = Reaction.objects.filter(to_user_id=user_id, from_user_id=fromuser_id)
    if(len(reactions) == 0):
        reaction = Reaction(to_user=UserInfo.objects.get(pk=user_id), from_user=UserInfo.objects.get(pk=fromuser_id), status=__status(reaction_status))
    else:
        reaction = reactions[0]
        reaction.status = __status(reaction_status)
    reaction.save()

def __status(status):
    if(status == "like"):
        return 0
    return 1
