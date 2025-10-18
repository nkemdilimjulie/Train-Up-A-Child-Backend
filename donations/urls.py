
 # donations/urls.py
from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import DonationViewSet, stripe_webhook, create_checkout_session

# RESTful donation endpoints (list, retrieve, etc.)
router = DefaultRouter()
router.register(r"", DonationViewSet, basename="donation")

urlpatterns = [
    # Stripe checkout session (POST from frontend when user clicks "Donate")
    path("create-checkout-session/", create_checkout_session, name="create-checkout-session"),

    # Stripe webhook (for confirming completed payments)
    path("webhook/", stripe_webhook, name="stripe-webhook"),
]

# Include router routes for DonationViewSet
urlpatterns += router.urls
