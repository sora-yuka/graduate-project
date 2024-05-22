from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SavedViewSet


router = DefaultRouter()
router.register("saved", SavedViewSet)

urlpatterns = [
    path("", include(router.urls))
]