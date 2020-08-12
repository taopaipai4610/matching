from django.db import models
from django.contrib.auth.models import User
from match.models.image import Image


class UserInfo(models.Model):
    image = models.OneToOneField(Image, on_delete=models.CASCADE) # 画像
    id = models.IntegerField(primary_key=True) # id
    name = models.CharField(max_length=100) # 名前
    self_introduction = models.CharField(max_length=500) # 自己紹介文
    sex = models.CharField(max_length=2) # 性別
    created_at = models.DateField(auto_now_add=True) # 作成日
    objects = models.Manager # ???
