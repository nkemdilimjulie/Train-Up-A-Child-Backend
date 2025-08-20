from django.urls import path
from .views import ChildListCreateView#, ChildDetailView

urlpatterns = [
    path("children/", ChildListCreateView.as_view(), name="child-list"),
    # path("children/<int:pk>/", ChildDetailView.as_view(), name="child-detail"),
]
    

