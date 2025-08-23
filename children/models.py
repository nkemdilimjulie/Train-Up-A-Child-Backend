from django.db import models
from sponsor.models import SponsorProfile

class Child(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.PositiveIntegerField(blank=True, null=True, default=3)
    story = models.TextField(blank=True, null=True)  # ✅ optional
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    registered_at = models.DateTimeField(auto_now_add=True)
    sponsor = models.ForeignKey(
        SponsorProfile,
        on_delete=models.SET_NULL,
        null=True, blank=True,
        related_name="children"
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

