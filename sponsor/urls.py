from django.urls import path
from .views import SponsorProfileListView, SponsorProfileDetailView

urlpatterns = [
    path("sponsors/", SponsorProfileListView.as_view(), name="sponsor-list"),
    path("sponsors/<int:pk>/", SponsorProfileDetailView.as_view(), name="sponsor-detail"),
]
