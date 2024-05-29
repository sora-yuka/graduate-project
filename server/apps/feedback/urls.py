from django.urls import path
from .views import rating_view


urlpatterns = [
    path("rate/", rating_view)
]