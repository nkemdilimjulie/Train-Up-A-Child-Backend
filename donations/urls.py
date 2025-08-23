from django.urls import path
from .views import DonationCreateView, DonationListView

urlpatterns = [
    path("donate/", DonationCreateView.as_view(), name="donation-create"),
    path("donations/", DonationListView.as_view(), name="donation-list"),
]
