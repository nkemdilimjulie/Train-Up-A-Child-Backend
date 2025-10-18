# children/views.py
from rest_framework import viewsets, permissions
from .models import Child
from .serializers import ChildSerializer

class ChildViewSet(viewsets.ModelViewSet):
    queryset = Child.objects.all().order_by("-date_registered")
    serializer_class = ChildSerializer
    permission_classes = [permissions.AllowAny]
