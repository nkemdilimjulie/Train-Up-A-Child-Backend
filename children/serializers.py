from rest_framework import serializers
from .models import Child
from donations.models import Donation


class ChildSerializer(serializers.ModelSerializer):
    """shows all sponsors who donated to the child"""
    sponsors = serializers.SerializerMethodField()

    class Meta:
        model = Child
        fields = ["id", "first_name", "last_name", "story", "balance", "registered_at", "sponsors"]

    def get_sponsors(self, obj):
        """Return unique sponsors who donated to this child"""
        donations = Donation.objects.filter(child=obj).select_related("sponsor")
        sponsors = {donation.sponsor for donation in donations}
        return [{"id": sponsor.id, "organization_name": sponsor.organization_name, "user": sponsor.user.username}
                for sponsor in sponsors]
