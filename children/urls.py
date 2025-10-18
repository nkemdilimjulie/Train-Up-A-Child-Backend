# children/urls.py
from rest_framework.routers import DefaultRouter
from .views import ChildViewSet

router = DefaultRouter()
router.register(r"", ChildViewSet, basename="child")

urlpatterns = router.urls


