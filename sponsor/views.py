from rest_framework import generics
from .models import SponsorProfile
from .serializers import SponsorProfileSerializer

class SponsorProfileListCreateView(generics.ListCreateAPIView):
    queryset = SponsorProfile.objects.all()
    serializer_class = SponsorProfileSerializer
    # permission_classes = []  # Adjust permissions as needed