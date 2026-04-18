
# donations/urls.py
from django.urls import path
from . import views
from .views import SponsorDonationListView
from .webhook import stripe_webhook

urlpatterns = [
    # Anonymous donation (no login required)
    path("checkout/", views.create_checkout_session, name="create_checkout_session"),

    # Sponsor donation (only for logged-in users)
    path("sponsor-checkout/", views.create_sponsor_checkout_session, name="create_sponsor_checkout_session"),

    # Get all donations by a specific user (for dashboard)
    path("user/<str:username>/", views.get_donations_by_user, name="get_donations_by_user"),
    
    path("", SponsorDonationListView.as_view()),
    
    path("webhook/", stripe_webhook),
]
