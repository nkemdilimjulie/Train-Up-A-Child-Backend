# donations/serializers.py
from rest_framework import serializers
from .models import Donation

class DonationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Donation
        fields = ["id", "user", "sponsor", "amount", "created_at", "stripe_payment_intent"]
