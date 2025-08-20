from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import Sponsor, Child
from .serializers import SponsorSerializer, ChildSerializer, DonationSerializer
from .services import safe_donation


class SponsorListCreateView(generics.ListCreateAPIView):
    queryset = Sponsor.objects.all()
    serializer_class = SponsorSerializer


class ChildListCreateView(generics.ListCreateAPIView):
    queryset = Child.objects.all()
    serializer_class = ChildSerializer


class DonationCreateView(generics.CreateAPIView):
    serializer_class = DonationSerializer

    def create(self, request, *args, **kwargs):
        sponsor_id = request.data.get("sponsor")
        child_id = request.data.get("child")
        amount = request.data.get("amount")

        sponsor = Sponsor.objects.get(id=sponsor_id)
        child = Child.objects.get(id=child_id)

        donation = safe_donation(child, sponsor, float(amount))
        serializer = self.get_serializer(donation)

        return Response(serializer.data, status=status.HTTP_201_CREATED)
    