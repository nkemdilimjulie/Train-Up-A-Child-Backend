from django.urls import path
from .views import sponsor_by_username

urlpatterns = [
    path("by-username/<str:username>/", sponsor_by_username, name="sponsor-by-username"),
]
