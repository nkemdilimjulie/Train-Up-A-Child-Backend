# children/urls.py

from django.urls import path
from .views import create_child_profile, list_children, update_child_profile


urlpatterns = [
    path("create/", create_child_profile, name="create_child_profile"),
    path("list/", list_children, name="list_children"),
    path("update/<int:pk>/", update_child_profile, name="update_child_profile"),
]
