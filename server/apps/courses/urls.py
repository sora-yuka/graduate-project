from django.urls import path, include
from rest_framework_nested.routers import NestedDefaultRouter
from rest_framework.routers import DefaultRouter
from .views import (
    CategoryListView,
    AllCourseViewSet,
    CourseViewSet,
    CourseItemViewSet,
    LatestCourseViewSet,
    MyCoursesListView
)


router = DefaultRouter()
router.register("category", CategoryListView)
router.register("page", CourseViewSet, basename="detailed")
router.register("latest", LatestCourseViewSet, basename="latest")
router.register("", AllCourseViewSet, basename="main")

item_router = NestedDefaultRouter(parent_router=router, parent_prefix="page", lookup="course")
item_router.register("item", CourseItemViewSet)

urlpatterns = [
    path("my-course/", MyCoursesListView.as_view()),
    path("saves/", CourseViewSet.as_view({"get": "get_saves"})),
    path("page/<int:pk>/save/", CourseViewSet.as_view({"post": "save_course"})),
    path("page/<int:pk>/like/", CourseViewSet.as_view({"post": "like_course"})),
    path("", include(router.urls)),
    path("", include(item_router.urls)),
]