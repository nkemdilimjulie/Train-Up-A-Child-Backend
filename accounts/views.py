from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth import authenticate, get_user_model
from .serializers import RegisterSerializer
from rest_framework.authtoken.models import Token

User = get_user_model()

@api_view(["POST"])
@permission_classes([AllowAny])
def register_user(request):
    serializer = RegisterSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        return Response({"success": True, "message": "Registration successful", "username": user.username}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["POST"])
@permission_classes([AllowAny])
def login_user(request):
    username = request.data.get("username")
    password = request.data.get("password")
    if not username or not password:
        return Response({"error":"Username and password required."}, status=status.HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    if user is None:
        return Response({"error":"Invalid credentials."}, status=status.HTTP_401_UNAUTHORIZED)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({
        "success": True,
        "message": f"Welcome back, {user.username}!",
        "token": token.key,
        "username": user.username,
        "is_sponsor": user.is_sponsor,
        "is_guest": user.is_guest,
        "is_child": user.is_child,
    })
