from django.contrib.auth import authenticate, get_user_model
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from .serializers import RegisterSerializer

User = get_user_model()

# --------------------
# REGISTER USER — only creates base User, not profiles
# --------------------
@api_view(["POST"])
@permission_classes([AllowAny])
def register_user(request):
    serializer = RegisterSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()

        # Adjust guest flag logically
        if user.is_sponsor or user.is_child:
            user.is_guest = False
            user.save()

        # Create auth token
        token, _ = Token.objects.get_or_create(user=user)

        return Response({
            "success": True,
            "message": "Registration successful",
            "username": user.username,
            "is_sponsor": user.is_sponsor,
            "is_guest": user.is_guest,
            "is_child": user.is_child,
            "token": token.key,
        }, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# --------------------
# LOGIN USER — no change
# --------------------
@api_view(["POST"])
@permission_classes([AllowAny])
def login_user(request):
    username = request.data.get("username")
    password = request.data.get("password")

    if not username or not password:
        return Response({"error": "Please provide both username and password."}, status=status.HTTP_400_BAD_REQUEST)

    user = authenticate(username=username, password=password)
    if user is None:
        return Response({"error": "Invalid username or password."}, status=status.HTTP_401_UNAUTHORIZED)

    token, _ = Token.objects.get_or_create(user=user)

    return Response({
        "message": "Login successful",
        "username": user.username,
        "is_sponsor": user.is_sponsor,
        "is_guest": user.is_guest,
        "is_child": user.is_child,
        "token": token.key,
    })

@api_view(["GET"])
@permission_classes([AllowAny])
def user_info(request):
    username = request.query_params.get("username")
    try:
        user = User.objects.get(username=username)
        return Response({
            "first_name": user.first_name,
            "last_name": user.last_name,
            "email": user.email
        })
    except User.DoesNotExist:
        return Response({"error": "User not found"}, status=404)
