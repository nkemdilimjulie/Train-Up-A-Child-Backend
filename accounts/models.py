from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    address = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    is_sponsor = models.BooleanField(default=False)
    is_guest = models.BooleanField(default=True)
    is_child = models.BooleanField(default=False)

    def __str__(self):
        return self.username
