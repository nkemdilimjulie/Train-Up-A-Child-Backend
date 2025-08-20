# Serializers convert models ↔ JSON (for DRF APIs).

from rest_framework import serializers
from .models import Sponsor, Child, Donation


class SponsorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sponsor
        fields = "__all__"


class ChildSerializer(serializers.ModelSerializer):
    class Meta:
        model = Child
        fields = "__all__"
        extra_kwargs = {
            "story": {"required": False},   # ✅ optional in API
        }



class DonationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Donation
        fields = "__all__"