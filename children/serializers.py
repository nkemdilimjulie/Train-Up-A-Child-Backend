from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import ChildProfile

User = get_user_model()

class ChildProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(write_only=True)
    first_name = serializers.CharField(source="user.first_name", read_only=True)
    last_name = serializers.CharField(source="user.last_name", read_only=True)
    email = serializers.EmailField(source="user.email", read_only=True)

    class Meta:
        model = ChildProfile
        fields = [
            "username", "first_name", "last_name", "email",
            "age", "class_name", "guardian_name", "guardian_phone", "guardian_email", "story"
        ]

    def create(self, validated_data):
        username = validated_data.pop("username")
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise serializers.ValidationError({"username": "User not found."})

        profile, created = ChildProfile.objects.get_or_create(user=user, defaults=validated_data)
        if not created:
            raise serializers.ValidationError({"detail": "Child profile already exists."})
        return profile
