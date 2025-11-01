# donations/models.py
from django.db import models
from django.conf import settings
from sponsors.models import SponsorProfile

class Donation(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    sponsor = models.ForeignKey(
        SponsorProfile,
        on_delete=models.CASCADE,
        related_name="donations",
        null=True,  # optional at first
        blank=True
    )
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    stripe_payment_intent = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.user} donated {self.amount}"
