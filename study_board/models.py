from django.contrib.auth.models import User
from django.db import models
from datetime import datetime, date
from django.utils.timezone import now


class Study_Board(models.Model):
    title = models.CharField(max_length=40, null=True)
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    date = models.DateTimeField(default=now)

    def __str__(self):
        return self.title
