from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class SponsorProfile(models.Model):
    """shows the total donated per sponsor automatically"""
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="sponsor_profile")
    organization_name = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    address = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.organization_name or self.user.get_full_name() or self.user.username

    @property
    def total_donated(self):
        """Calculate total donations made by this sponsor"""
        return sum(donation.amount for donation in self.donations.all())
