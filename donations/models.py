from django.db import models
from children.models import Child
from sponsor.models import SponsorProfile

class Donation(models.Model):
    sponsor = models.ForeignKey(SponsorProfile, on_delete=models.CASCADE, related_name="donations")
    child = models.ForeignKey(Child, on_delete=models.CASCADE, related_name="donations")
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    donated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sponsor} donated {self.amount} to {self.child}"

