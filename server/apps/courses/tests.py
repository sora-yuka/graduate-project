from typing import Dict
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model

from .models import CoursesModel, CategoryModel

# Create your tests here.

User = get_user_model()


class CourseTest(APITestCase):
    base_url = "http://localhost:8000/api/v1/courses/"
    
    @property
    def example_bearer_token(self) -> Dict[str, str]:
        user = User.objects.create_user(
            email = "obawuwi@vonsoru.tz",
            password = "practice",
            is_active = True
            )
        refresh = RefreshToken.for_user(user)
        return {"HTTP_AUTHORIZATION": f"Bearer: {refresh.access_token}"}
    
    def create_user(self) -> User:
        user = User.objects.create_user(
            email = "anueja@pavla.edu",
            password = "keepeye",
            is_active = True
        )
        return user
    
    def create_course(self) -> CoursesModel:
        user = self.create_user()
        category = CategoryModel.objects.create(category="study")
        course = CoursesModel.objects.create(
            owner = user,
            title = "shinning",
            description = "cloth on enough pocket spent task funny nearby led poem prevent plan birds tightly onto twice surprise nearly forgotten till week step park does",
            level = "Beginner",
            category = category
        )
        return course
    
    def test_get_courses(self) -> None:
        response = self.client.get(path=self.base_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_create_courses(self) -> None:
        url = self.base_url + "page/"
        course = self.create_course()
        response = self.client.post(path=url, data={
            "owner": course.owner.id,
            "title": course.title,
            "description": course.description,
            "level": course.level,
            "category": course.category.id,
            "preview_image": "/blanks/NETFILX_wallpaper.jpg"
            }, **self.example_bearer_token)
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, response.data)