from typing import Dict
from uuid import uuid4
from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status

# Create your tests here.

User = get_user_model()


class AccountTest(APITestCase):
    base_url = "http://localhost:8000/api/v1/user/"
    
    @property
    def example_bearer_token(self) -> Dict[str, str]:
        user = User.objects.create_user(
            email = "example@mail.com",
            password = "qwerty",
            is_active = True,
            )
        refresh = RefreshToken.for_user(user)
        return {"HTTP_AUTHORIZATION": f"Bearer: {refresh.access_token}"}
    
    def create_user(self, state: bool) -> User:
        user = User.objects.create_user(
            email = "example@mail.com",
            password = "qwerty",
            is_active = state
        )
        return user
    
    def test_register_account(self) -> None:
        url = self.base_url + "register/"
        response = self.client.post(path=url, data={
            "email": "user@gmail.com",
            "password": "qwerty",
            "password_confirm": "qwerty"
            })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_verify_account(self) -> None:
        user = self.create_user(False)
        url = self.base_url + f"verify/{user.verification_code}/"
        response = self.client.get(path=url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_login_account(self) -> None:
        self.create_user(True)
        url = self.base_url + "login/"
        response = self.client.post(path=url, data={
            "email": "example@mail.com",
            "password": "qwerty"
            })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        