from rest_framework import serializers
from .models import SponsorProfile

class SponsorProfileSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.username', read_only=True)
    class Meta:
        model = SponsorProfile
        fields = ["id","user","organization_name","phone","address"]
