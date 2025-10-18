from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

class SponsorProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="sponsor_profile")
    organization_name = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=30, blank=True, null=True)
    address = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.organization_name or self.user.username
