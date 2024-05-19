from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    AllCoursesListAPIView, 
    CategoryCoursesListAPIView,
    AllUserCoursesListAPIView,
    CourseViewSet,
    CourseItemViewSet,
    # CourseItemListAPIView,
)


router = DefaultRouter()
# router.register("item", CourseItemViewSet)
router.register(r'(?P<course>\d+)/item', CourseItemViewSet, basename="courseitem")
router.register("", CourseViewSet)

urlpatterns = [
    path("", AllCoursesListAPIView.as_view()),
    path("category/<str:category>/", CategoryCoursesListAPIView.as_view()),
    path("profile/<str:profile>/", AllUserCoursesListAPIView.as_view()),
    path("crud/", include(router.urls)),
    # path("crud/<str:course>/item/")
]