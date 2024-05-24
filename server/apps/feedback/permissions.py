from rest_framework.permissions import BasePermission
from rest_framework.views import APIView
from django.http import HttpRequest


class IsFeedBackOwner(BasePermission):
    def has_object_permission(self, request: HttpRequest, view, obj) -> bool:
         return request.user.is_authenticated and request.user == obj.owner