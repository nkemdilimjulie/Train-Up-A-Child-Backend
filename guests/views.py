from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework import status
from .models import GuestProfile

User = get_user_model()

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def me_guest(request):
    try:
        guest = GuestProfile.objects.get(user=request.user)
        return Response({"username": request.user.username})
    except GuestProfile.DoesNotExist:
        return Response({"error":"Guest profile not found"}, status=status.HTTP_404_NOT_FOUND)
