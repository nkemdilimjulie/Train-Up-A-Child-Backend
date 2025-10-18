# children/serializers.py
from rest_framework import serializers
from .models import Child

class ChildSerializer(serializers.ModelSerializer):
    class Meta:
        model = Child
        fields = [
            "id",
            "username",
            "first_name",
            "last_name",
            "age",
            "class_name",
            "address",
            "guardian_name",
            "guardian_email",
            "guardian_phone",
            "story",
            "photo",
            "date_registered",
        ]
