from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class UserProfile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)
    mobile = models.CharField(max_length=20, null=True)
    address = models.CharField(max_length=250, null=True)
    city = models.CharField(max_length=100, null=True)
    state = models.CharField(max_length=100, null=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def __str__(self):
        return self.user.username
