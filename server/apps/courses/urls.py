from django.urls import path
from .views import AllCoursesListAPIView


urlpatterns = [
    path("", AllCoursesListAPIView.as_view())
]