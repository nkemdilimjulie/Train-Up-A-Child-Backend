from rest_framework import serializers
from .models import SponsorProfile
from donations.models import Donation
from children.serializers import ChildSerializer

class SponsorProfileSerializer(serializers.ModelSerializer):
    """shows total donations and lists the children the sponsor supports (via donations)"""
    total_donated = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)
    supported_children = serializers.SerializerMethodField()

    class Meta:
        model = SponsorProfile
        fields = ["id", "user", "organization_name", "phone", "address", "total_donated", "supported_children"]

    def get_supported_children(self, obj):
        """Return unique children this sponsor has donated to"""
        donations = Donation.objects.filter(sponsor=obj).select_related("child")
        children = {donation.child for donation in donations}
        return ChildSerializer(children, many=True).data
