from django.urls import path
from .views import create_guest_profile
# from .views import me_guest, all_guests

urlpatterns = [
    # path("me/", me_guest, name="me_guest"),
    # path("all/", all_guests, name="all_guests"),
    path("", create_guest_profile, name="create_guest_profile"),
]
