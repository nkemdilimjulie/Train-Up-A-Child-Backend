from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import GuestProfile

User = get_user_model()

class GuestProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(write_only=True)

    class Meta:
        model = GuestProfile
        fields = ["username", "first_name", "last_name", "email"]

    def create(self, validated_data):
        username = validated_data.pop("username")
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise serializers.ValidationError({"username": "User not found."})

        profile, created = GuestProfile.objects.get_or_create(user=user, defaults=validated_data)
        if not created:
            raise serializers.ValidationError({"detail": "Guest profile already exists."})
        return profile
