import logging
from django.shortcuts import render
from django.db.utils import IntegrityError
from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status

from .serializers import UserRegisterSerializer
from .tasks import send_verification_code
from apps.profiles.models import UserProfile

# Create your views here.

User = get_user_model()


class RegisterAPIView(APIView):
    permission_classes = [AllowAny]
    
    def post(self, request: Request) -> Response:
        try:
            serializer = UserRegisterSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            user = serializer.save()
            # logger.info(f"User registered successfully. User-data: {user}")
        except IntegrityError:
            # logger.error(f"User doesn't registered. User-data: {user}")
            return Response({
                "MESSAGE": "Something went wrong, please check the input",
                "STATUS": status.HTTP_400_BAD_REQUEST
            }, status=status.HTTP_400_BAD_REQUEST)
        
        send_verification_code.delay(user.email, user.verification_code)
        return Response({
            "SERIALIZER DATA": serializer.data,
            "MESSAGE": "User created successfully",
            "STATUS": status.HTTP_201_CREATED
        }, status=status.HTTP_201_CREATED)
    

class VerifyAccountAPIView(APIView):
    permission_classes = [AllowAny]
    
    def get(self, request: Request, verification_code: str) -> Response:
        try:
            user = User.objects.get(verification_code=verification_code)
            user.is_active = True
            user.verification_code = ""
            UserProfile.objects.create(owner=user)
            user.save()
            return Response({
                "MESSAGE": "Account activated successfully!",
                "STATUS": status.HTTP_200_OK
            }, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({
                "MESSAGE": "User with given email doesn't exist",
                "STATUS": status.HTTP_400_BAD_REQUEST
            }, status=status.HTTP_400_BAD_REQUEST)