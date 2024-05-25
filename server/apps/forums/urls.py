from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import ForumViewSet, ForumAnswerViewSet


router = DefaultRouter()
router.register("answer", ForumAnswerViewSet)
router.register("", ForumViewSet)

urlpatterns = [
    path("", include(router.urls))
]