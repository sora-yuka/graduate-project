from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    AllCourseViewSet,
    CourseViewSet,
    CourseItemViewSet,
    LatestCourseViewSet
)


router = DefaultRouter()
router.register("item", CourseItemViewSet)
router.register("latest", LatestCourseViewSet, basename="latest")
router.register("detailed", CourseViewSet)
router.register("", AllCourseViewSet, basename="main")

urlpatterns = [
    path("", include(router.urls)),
]