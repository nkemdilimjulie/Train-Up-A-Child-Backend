
from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["id","username","first_name","last_name","email","address","phone","password","is_sponsor","is_guest","is_child"]

    def create(self, validated_data):
        password = validated_data.pop("password")
        # default roles: if none provided, mark as guest
        if not validated_data.get("is_sponsor") and not validated_data.get("is_child"):
            validated_data["is_guest"] = True
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user
