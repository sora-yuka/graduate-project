from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CommentModelViewSet

router = DefaultRouter()
router.register("comment", CommentModelViewSet)

urlpatterns = [
    path("", include(router.urls))
]