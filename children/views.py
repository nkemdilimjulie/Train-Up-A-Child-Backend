# children/views.py

from rest_framework.decorators import api_view, permission_classes, parser_classes
from rest_framework.permissions import AllowAny
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import ChildProfile
from .serializers import ChildProfileSerializer


# ✅ Create Child Profile (with photo upload support)
@api_view(["POST"])
@permission_classes([AllowAny])
@parser_classes([MultiPartParser, FormParser])  # enables file upload
def create_child_profile(request):
    serializer = ChildProfileSerializer(data=request.data, context={"request": request})
    if serializer.is_valid():
        serializer.save()
        return Response(
            {"message": "Child profile created successfully!"},
            status=status.HTTP_201_CREATED,
        )
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# ✅ List all children (for frontend display)
@api_view(["GET"])
@permission_classes([AllowAny])
def list_children(request):
    children = ChildProfile.objects.all().order_by("-id")
    serializer = ChildProfileSerializer(children, many=True, context={"request": request})
    return Response(serializer.data, status=status.HTTP_200_OK)


# ✅ Update child profile (photo, story, etc.)
@api_view(["PATCH"])
@permission_classes([AllowAny])
@parser_classes([MultiPartParser, FormParser])
def update_child_profile(request, pk):
    child = get_object_or_404(ChildProfile, pk=pk)
    serializer = ChildProfileSerializer(child, data=request.data, partial=True, context={"request": request})
    if serializer.is_valid():
        serializer.save()
        return Response(
            {"message": "Child profile updated successfully!", "data": serializer.data},
            status=status.HTTP_200_OK,
        )
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
