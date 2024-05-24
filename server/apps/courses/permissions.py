from django.http import HttpRequest
from django.contrib.auth import get_user_model
from rest_framework.permissions import BasePermission, SAFE_METHODS
from rest_framework.views import APIView

User = get_user_model()


class IsCourseOwner(BasePermission):
    def has_object_permission(self, request: HttpRequest, view, obj) -> bool:
        if request.method in SAFE_METHODS:
            return True
        return request.user.is_authenticated and request.user == obj.course.owner
