
from django.urls import path
from .views import create_checkout_session, get_donations_by_user

urlpatterns = [
    path("checkout/", create_checkout_session, name="create_checkout_session"),
    path("<str:username>/", get_donations_by_user, name="get_donations_by_user"),
]
