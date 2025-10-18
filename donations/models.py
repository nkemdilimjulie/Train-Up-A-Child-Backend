from django.db import models
from sponsors.models import SponsorProfile

class Donation(models.Model):
    sponsor = models.ForeignKey(SponsorProfile, on_delete=models.CASCADE, related_name="donations")
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)
    stripe_session_id = models.CharField(max_length=255, blank=True, null=True)
    reference = models.CharField(max_length=120, blank=True, null=True)

    def __str__(self):
        return f"Donation by {self.sponsor.user.username} - {self.amount} on {self.date}"
