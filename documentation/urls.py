from django.urls import path
from .views import APIDocumentationView

urlpatterns = [
    path("docs/", APIDocumentationView.as_view(), name="api-docs"),
]
