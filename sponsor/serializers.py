from rest_framework import serializers
from .models import SponsorProfile

class SponsorProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = SponsorProfile
        fields = "__all__"
        # read_only_fields = ["joined_at"]