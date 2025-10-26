from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings


class User(AbstractUser):
    # user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="accounts_user")
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120, default="")
    email = models.EmailField(max_length=254, unique=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    password = models.CharField(max_length=128)
    is_sponsor = models.BooleanField(default=False)
    is_guest = models.BooleanField(default=True)
    is_child = models.BooleanField(default=False)

    def __str__(self):
        return self.username
