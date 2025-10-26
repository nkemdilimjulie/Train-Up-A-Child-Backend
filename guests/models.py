from django.db import models
from django.conf import settings

class GuestProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=120, blank=True, null=True)
    last_name = models.CharField(max_length=120, blank=True, null=True)
    email = models.EmailField(max_length=255, blank=True, null=True)

    
    
    def __str__(self):
        return f"Guest: {self.user.username}"
