from django.db import models
from django.contrib.auth.models import User


class Status(models.Model):
    status = models.TextField(null=True, max_length=250)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'status_+{self.user}'
