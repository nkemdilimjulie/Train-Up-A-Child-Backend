# children/urls.py

from django.urls import path
from .views import create_child_profile
from .views import list_children

urlpatterns = [
    path("create/", create_child_profile, name="create_child_profile"),
    path("list/", list_children, name="list_children"),
]
