from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import ChildProfile

User = get_user_model()

class ChildProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(write_only=True)
    first_name = serializers.CharField(source="user.first_name", read_only=True)
    last_name = serializers.CharField(source="user.last_name", read_only=True)
    email = serializers.EmailField(source="user.email", read_only=True)
    photo = serializers.ImageField(required=False, allow_null=True) # ✅ let DRF handle image URLs

    class Meta:
        model = ChildProfile
        fields = "__all__"

    # def get_photo(self, obj):
    #     request = self.context.get("request")
    #     if obj.photo:
    #         photo_url = obj.photo.url
    #     else:
    #         photo_url = "/media/children/photos/default.jpg"

    #     if request:
    #         if photo_url.startswith("/media/"):
    #             return request.build_absolute_uri(photo_url)
    #         else:
    #             return photo_url
    #     return photo_url


    def create(self, validated_data):
        username = validated_data.pop("username")
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise serializers.ValidationError({"username": "User not found."})

        if ChildProfile.objects.filter(user=user).exists():
            raise serializers.ValidationError({"detail": "Child profile already exists."})

        # ✅ Create new child profile (this properly handles uploaded files)
        profile = ChildProfile.objects.create(user=user, **validated_data)
        return profile
