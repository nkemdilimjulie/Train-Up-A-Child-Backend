from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model
from .models import SponsorProfile
from .serializers import SponsorProfileSerializer

User = get_user_model()

@api_view(["GET","POST"])
@permission_classes([IsAuthenticated])
def sponsor_by_username(request, username):
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return Response({"error":"User not found"}, status=status.HTTP_404_NOT_FOUND)
    # only allow user or admin
    if request.user != user and not request.user.is_staff:
        return Response({"error":"Forbidden"}, status=status.HTTP_403_FORBIDDEN)

    sponsor, created = SponsorProfile.objects.get_or_create(user=user)
    if request.method == "GET":
        serializer = SponsorProfileSerializer(sponsor)
        return Response(serializer.data)
    # POST -> update
    serializer = SponsorProfileSerializer(sponsor, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        # mark the user as sponsor
        if not user.is_sponsor:
            user.is_sponsor = True
            user.is_guest = False
            user.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
