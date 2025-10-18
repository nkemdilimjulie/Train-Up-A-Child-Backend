from django.db import models
from django.conf import settings

class GuestProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # any guest-specific fields can go here
    def __str__(self):
        return f"Guest: {self.user.username}"
