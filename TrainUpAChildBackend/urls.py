from django.contrib import admin
from django.urls import path, include
# from donations.webhooks import StripeWebhookView
from donations import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path("admin/", admin.site.urls),

    # API routes
    path("api/accounts/", include("accounts.urls")), 
    path("api/sponsors/", include("sponsors.urls")),
    path("api/children/", include("children.urls")),
    path("api/donations/", include("donations.urls")),
    path("api/guests/", include("guests.urls")),
    path("api/contact/", include("contact.urls")),
    
]   

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)