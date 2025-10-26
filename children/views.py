# # children/views.py

from .models import ChildProfile
from .serializers import ChildProfileSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status


@api_view(["POST"])
@permission_classes([AllowAny])
def create_child_profile(request):
    serializer = ChildProfileSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Child profile created successfully!"}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET"])
@permission_classes([AllowAny])
def list_children(request):
    children = ChildProfile.objects.all()
    serializer = ChildProfileSerializer(children, many=True)
    return Response(serializer.data)