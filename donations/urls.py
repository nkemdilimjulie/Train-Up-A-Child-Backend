from django.urls import path
from .views import SponsorListCreateView, ChildListCreateView, DonationCreateView

urlpatterns = [
    path("sponsors/", SponsorListCreateView.as_view(), name="sponsor-list"),
    path("children/", ChildListCreateView.as_view(), name="child-list"),
    path("donate/", DonationCreateView.as_view(), name="donation-create"),
]