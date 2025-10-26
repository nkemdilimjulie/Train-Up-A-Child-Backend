# from rest_framework.decorators import api_view, permission_classes
# from rest_framework.permissions import IsAuthenticated
# from django.contrib.auth import get_user_model
# from rest_framework.response import Response
# from rest_framework import status
# from .models import GuestProfile
# from .serializers import GuestProfileSerializer

# User = get_user_model()

# @api_view(["GET"])
# @permission_classes([IsAuthenticated])
# def me_guest(request):
#     try:
#         guest = GuestProfile.objects.get(user=request.user)
#         return Response({"username": request.user.username})
#     except GuestProfile.DoesNotExist:
#         return Response({"error":"Guest profile not found"}, status=status.HTTP_404_NOT_FOUND)

# @api_view(["GET"])
# @permission_classes([IsAuthenticated])
# def all_guests(request):
#     guests = GuestProfile.objects.all()
#     serializer = GuestProfileSerializer(guests, many=True)
#     return Response(serializer.data)

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from .serializers import GuestProfileSerializer

@api_view(["POST"])
@permission_classes([AllowAny])
def create_guest_profile(request):
    serializer = GuestProfileSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Guest profile created successfully!"}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
