from django.urls import path
from .views import create_guest_profile


urlpatterns = [
    path("", create_guest_profile, name="create_guest_profile"),
]
