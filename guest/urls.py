from django.urls import path
from .views import GuestChildListView

urlpatterns = [
    path("browse-children/", GuestChildListView.as_view(), name="guest-children"),
]
