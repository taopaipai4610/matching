from django.db import models


class ChatRoom(models.Model):
    id = models.AutoField(primary_key=True)
    objects = models.Manager