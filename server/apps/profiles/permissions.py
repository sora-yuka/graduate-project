from django.http import HttpRequest
from django.contrib.auth import get_user_model
from rest_framework.permissions import BasePermission
from rest_framework.views import APIView

from .models import UserProfile


class IsProfileOwner(BasePermission):
    def has_object_permission(
        self, 
        request: HttpRequest, 
        view: APIView, 
        obj: UserProfile
        ) -> bool:
        if request.method in SAFE_METHOD:
            return True
        return request.user.is_authenticated and request.user == obj.owner
