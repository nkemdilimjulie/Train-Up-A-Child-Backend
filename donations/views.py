from rest_framework import generics, status
from rest_framework.response import Response
from .models import Donation
from .serializers import DonationSerializer
from .services import safe_donation
from children.models import Child
from sponsor.models import SponsorProfile

class DonationCreateView(generics.CreateAPIView):
    serializer_class = DonationSerializer

    def create(self, request, *args, **kwargs):
        sponsor_id = request.data.get("sponsor_id")
        child_id = request.data.get("child_id")
        amount = request.data.get("amount")

        sponsor = SponsorProfile.objects.get(id=sponsor_id)
        child = Child.objects.get(id=child_id)

        donation = safe_donation(child, sponsor, float(amount))
        serializer = self.get_serializer(donation)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

class DonationListView(generics.ListAPIView):
    queryset = Donation.objects.all()
    serializer_class = DonationSerializer
