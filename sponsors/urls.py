from django.urls import path
from .views import create_sponsor_profile, get_sponsor_profile

urlpatterns = [
    path("", create_sponsor_profile, name="create_sponsor_profile"),
    path("<str:username>/", get_sponsor_profile, name="get_sponsor_profile"),
]
