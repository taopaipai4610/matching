from django.db import models
from match.models.userinfo import UserInfo


class Reaction(models.Model):
    id = models.IntegerField(primary_key=True)
    # いいねされた人
    to_user = models.ForeignKey(UserInfo, on_delete=models.CASCADE, related_name="toid")
    # いいねをした人
    from_user = models.ForeignKey(UserInfo, on_delete=models.CASCADE, related_name="fromid")
    status = models.IntegerField(primary_key=False)