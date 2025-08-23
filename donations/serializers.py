# Serializers convert models ↔ JSON (for DRF APIs).
from rest_framework import serializers
from .models import Donation
from sponsor.serializers import SponsorProfileSerializer
from children.serializers import ChildSerializer
from sponsor.models import SponsorProfile
from children.models import Child

class DonationSerializer(serializers.ModelSerializer):
    sponsor = SponsorProfileSerializer(read_only=True)
    child = ChildSerializer(read_only=True)

    sponsor_id = serializers.PrimaryKeyRelatedField(
        queryset=SponsorProfile.objects.all(), write_only=True, source="sponsor"
    )
    child_id = serializers.PrimaryKeyRelatedField(
        queryset=Child.objects.all(), write_only=True, source="child"
    )

    class Meta:
        model = Donation
        fields = ["id", "sponsor", "child", "sponsor_id", "child_id", "amount", "donated_at"]
