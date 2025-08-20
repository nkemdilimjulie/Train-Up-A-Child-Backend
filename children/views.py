from rest_framework import generics
from .models import Child
from .serializers import ChildSerializer

class ChildListCreateView(generics.ListCreateAPIView):
    queryset = Child.objects.all()
    serializer_class = ChildSerializer

