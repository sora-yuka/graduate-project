from django.urls import path
from .views import (
    RegisterAPIView,
    VerifyAccountAPIView
    )


urlpatterns = [
    path("register/", RegisterAPIView.as_view()),
    path("verify/<uuid:verification_code>/", VerifyAccountAPIView.as_view()),
    
]