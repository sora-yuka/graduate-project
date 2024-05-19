from typing import Dict
from rest_framework import serializers
from django.contrib.auth import get_user_model

from .models import CoursesModel, CourseItemModel, CategoryModel
from apps.profiles.models import UserProfile

User = get_user_model()


class AllCoursesSerialier(serializers.ModelSerializer):
    
    class Meta:
        model = CoursesModel
        fields = ["id", "owner", "owner_profile", "title", "preview_image", "category"]
        
    def to_representation(self, instance: CoursesModel) -> Dict[str, str]:
        representation = super().to_representation(instance)
        user = User.objects.get(id=representation["owner"])
        profile = UserProfile.objects.get(id=representation["owner_profile"])
        category = CategoryModel.objects.get(id=representation["category"])
        representation["owner"] = {"id": user.id, "email": user.email}
        representation["owner_profile"] = {"profile_id": profile.id, "profile_username": profile.username}
        representation["category"] = {"id": category.id, "category": category.category}
        return representation
    

class CategorySerializer(serializers.ModelSerializer):
    all_courses = AllCoursesSerialier(many=True, read_only=True)
    
    class Meta:
        model = CategoryModel
        fields = ["id", "owner", "owner_profile", "title", "preview_image", "category"]
    
    def to_representation(self, instance: CoursesModel) -> Dict[str, str]:
        representation = super().to_representation(instance)
        user = User.objects.get(id=representation["owner"])
        profile = UserProfile.objects.get(id=representation["owner_profile"])
        category = CategoryModel.objects.get(id=representation["category"])
        representation["owner"] = {"id": user.id, "email": user.email}
        representation["owner_profile"] = {"profile_id": profile.id, "profile_username": profile.username}
        representation["category"] = {"id": category.id, "category": category.category}
        return representation
    

class CourseSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CoursesModel
        fields = [
            "id", 
            "title", 
            "description",
            "level",
            "preview_image",
            "category",
        ]
        
    def to_representation(self, instance: CoursesModel) -> Dict[str, str]:
        representation = super().to_representation(instance)
        category = CategoryModel.objects.get(id=representation["category"])
        representation["category"] = {"id": category.id, "category": category.category}
        return representation
    
    
class CourseItemSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CourseItemModel
        fields = "__all__"
        
    def to_representation(self, instance: CourseItemModel) -> Dict[str, str]:
        representation = super().to_representation(instance)
        # unfiltered_course = CourseItemModel.objects.filter(course=instance.id)
        # course = CourseItemSerializer(unfiltered_course, many=True).data
        representation["course"] = {"id": instance.id, "name": instance.name}
        return representation