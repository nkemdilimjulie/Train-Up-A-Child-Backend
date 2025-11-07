from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.db.models import Sum
from .models import SponsorProfile
from donations.models import Donation

User = get_user_model()

class SponsorProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(write_only=True)
    first_name = serializers.CharField(source="user.first_name", read_only=True)
    last_name = serializers.CharField(source="user.last_name", read_only=True)
    email = serializers.EmailField(source="user.email", read_only=True)

    total_donated = serializers.SerializerMethodField()

    class Meta:
        model = SponsorProfile
        fields = ["username", "first_name", "last_name", "email", "organization", "phone", "address", "country", "total_donated"]


    def create(self, validated_data):
        username = validated_data.pop("username")
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise serializers.ValidationError({"username": "User not found."})

        profile, created = SponsorProfile.objects.get_or_create(user=user, defaults=validated_data)
        if not created:
            raise serializers.ValidationError({"detail": "Sponsor profile already exists."})
        return profile


    def get_total_donated(self, obj):
        """
        Returns the total donations made by this sponsor.
        """
        total = Donation.objects.filter(sponsor=obj).aggregate(total_amount=Sum('amount'))['total_amount']
        return total or 0
   
    