from django.urls import path, include
from rest_framework_nested.routers import NestedDefaultRouter
from rest_framework.routers import DefaultRouter
from .views import (
    AllCourseViewSet,
    CourseViewSet,
    CourseItemViewSet,
    LatestCourseViewSet
)


router = DefaultRouter()
router.register("page", CourseViewSet, basename="detailed")
router.register("latest", LatestCourseViewSet, basename="latest")
router.register("", AllCourseViewSet, basename="main")

item_router = NestedDefaultRouter(parent_router=router, parent_prefix="page", lookup="course")
item_router.register("item", CourseItemViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("", include(item_router.urls)),
]