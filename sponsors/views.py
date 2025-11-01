# sponsors/views.py
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from .models import SponsorProfile
from .serializers import SponsorProfileSerializer

@api_view(["POST"])
@permission_classes([AllowAny])
def create_sponsor_profile(request):
    serializer = SponsorProfileSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Sponsor profile created successfully!"}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET"])
@permission_classes([AllowAny])
def get_sponsor_profile(request, username):
    """
    Retrieve sponsor profile by username.
    """
    try:
        sponsor = SponsorProfile.objects.select_related("user").get(user__username=username)
        serializer = SponsorProfileSerializer(sponsor)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except SponsorProfile.DoesNotExist:
        return Response({"error": "Sponsor not found"}, status=status.HTTP_404_NOT_FOUND)
