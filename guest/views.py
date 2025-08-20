from rest_framework import generics
from donations.models import Child
from donations.serializers import ChildSerializer

class GuestChildListView(generics.ListAPIView):
    queryset = Child.objects.all()
    serializer_class = ChildSerializer
