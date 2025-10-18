from django.contrib import admin
from django.urls import path, include
# from donations.webhooks import StripeWebhookView
from donations import views

urlpatterns = [
    path("admin/", admin.site.urls),

    # API routes
    path("api/accounts/", include("accounts.urls")), 
    path("api/sponsors/", include("sponsors.urls")),
    path("api/children/", include("children.urls")),
    path("api/donations/", include("donations.urls")),
    path("api/guest-view-children/", include("guests.urls")),
    
    # Stripe webhook endpoint for handling payment events
    path("webhook/", views.stripe_webhook, name="stripe-webhook"), # root-level webhook
]   
