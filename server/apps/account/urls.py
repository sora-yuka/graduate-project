from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import (
    RegisterAPIView,
    VerifyAccountAPIView
)


urlpatterns = [
    path("register/", RegisterAPIView.as_view()),
    path("verify/<uuid:verification_code>/", VerifyAccountAPIView.as_view()),
    path("login/", TokenObtainPairView.as_view(), name="token_obtain"),
    path("refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]