from django.shortcuts import render
from rest_framework.exceptions import NotFound
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet, ModelViewSet
from rest_framework.mixins import CreateModelMixin, UpdateModelMixin, DestroyModelMixin

from .models import CoursesModel, CourseItemModel, CategoryModel
from .serializers import AllCoursesSerialier, CategorySerializer, CourseSerializer, CourseItemSerializer
from .permissions import IsCourseOwner
from apps.profiles.models import UserProfile

# Create your views here.


class AllCoursesListAPIView(ListAPIView):
    serializer_class = AllCoursesSerialier
    queryset = CoursesModel.objects.all()
    
    
class CategoryCoursesListAPIView(ListAPIView):
    serializer_class = AllCoursesSerialier
    
    def get_queryset(self) -> CoursesModel | None:
        try:
            category_name = self.kwargs["category"]
            category = CategoryModel.objects.get(category=category_name.lower())
            return CoursesModel.objects.filter(category=category)
        except CategoryModel.DoesNotExist:
            raise NotFound("Category not found.")
        
        
class AllUserCoursesListAPIView(ListAPIView):
    serializer_class = AllCoursesSerialier
    
    def get_queryset(self) -> CoursesModel | None:
        try:
            profile_username = self.kwargs["profile"]
            profile = UserProfile.objects.get(username=profile_username)
            return CoursesModel.objects.filter(owner_profile=profile)
        except UserProfile.DoesNotExist:
            raise NotFound("User not found.")
        
    
class CourseViewSet(
    CreateModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
    GenericViewSet
):
    permission_classes = [IsCourseOwner]
    serializer_class = CourseSerializer
    queryset = CoursesModel.objects.all()
    
    def perform_create(self, serializer: CourseSerializer) -> None:
        profile = UserProfile.objects.get(owner=self.request.user)
        serializer.save(owner=self.request.user, owner_profile=profile)
        
    
class CourseItemViewSet(ModelViewSet):
    permission_classes = [IsCourseOwner]
    serializer_class = CourseItemSerializer
    
    def get_queryset(self) -> CourseItemModel | None:
        course_name = self.kwargs["course"]
        return CourseItemModel.objects.filter(course=course_name)