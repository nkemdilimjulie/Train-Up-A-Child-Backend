from django.urls import path
from .views import SponsorProfileListCreateView

urlpatterns = [
    path("sponsor-profiles/", SponsorProfileListCreateView.as_view(), name="sponsor-profile-list"),
]
