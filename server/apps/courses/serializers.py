from typing import Dict
from datetime import datetime
from rest_framework import serializers
from django.contrib.auth import get_user_model

from .models import CoursesModel, CourseItemModel, CategoryModel
from apps.profiles.models import UserProfile

User = get_user_model()


class AllCoursesSerialier(serializers.ModelSerializer):
    
    class Meta:
        model = CoursesModel
        fields = ["id", "owner", "title", "preview_image", "level", "category"]
        
    def to_representation(self, instance: CoursesModel) -> Dict[str, str]:
        representation = super().to_representation(instance)
        user = User.objects.get(id=representation["owner"])
        profile = UserProfile.objects.get(owner=user)
        category = CategoryModel.objects.get(id=representation["category"])
        
        representation.update({
            "owner": {"id": user.id, "email": user.email},
            "owner_profile": {"profile_id": profile.id, "profile_username": profile.username},
            "category": {"id": category.id, "category": category.category},
        })
        return representation
    

class CategorySerializer(serializers.ModelSerializer):
    all_courses = AllCoursesSerialier(many=True, read_only=True)
    
    class Meta:
        model = CategoryModel
        fields = "__all__"
    
    def to_representation(self, instance: CoursesModel) -> Dict[str, str]:
        representation = super().to_representation(instance)
        representation["category"] = {"id": category.id, "category": category.category}
        return representation
    

class DetailedCourseSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CoursesModel
        fields = "__all__"
        
    def to_representation(self, instance: CoursesModel) -> Dict[str, str]:
        representation = super().to_representation(instance)
        
        category = CategoryModel.objects.get(id=representation["category"])
        courses_item = CourseItemModel.objects.filter(course=instance.id)
        
        recommendations = CoursesModel.objects.filter(category=instance.category)
        recommendation_data = [{
            "id": recommended_course.id,
            "owner": UserProfile.objects.get(owner=recommended_course.owner).username,
            "title": recommended_course.title,
            "level": recommended_course.level,
            "preview_image": "http://localhost:8000/" + recommended_course.preview_image.url,
            "category": {
                "id": recommended_course.category.id,
                "category": recommended_course.category.category
                }
            } for recommended_course in recommendations if recommended_course.id != instance.id
            ]
            
        representation.update({
            "owner": UserProfile.objects.get(owner=instance.owner).username,
            "created_at": instance.created_at.strftime("%d.%m.%Y"),
            "updated_at": instance.updated_at.strftime("%d.%m.%Y"),
            "category": {"id": category.id, "category": category.category},
            "course_items": CourseItemSerializer(courses_item, many=True).data,
            "recommendation": recommendation_data
        })
        return representation
    
    
class CourseItemSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CourseItemModel
        fields = "__all__"
        
    def to_representation(self, instance: CourseItemModel) -> Dict[str, str]:
        representation = super().to_representation(instance)
        representation["course"] = {"id": instance.id, "name": instance.name}
        return representation