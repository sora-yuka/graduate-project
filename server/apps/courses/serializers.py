from typing import Dict
from datetime import datetime

from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.db.models import Avg

from .models import CoursesModel, CourseItemModel, CategoryModel
from apps.profiles.models import UserProfile

User = get_user_model()


class AllCoursesSerialier(serializers.ModelSerializer):
    
    class Meta:
        model = CoursesModel
        fields = ["id", "owner", "title", "preview_image", "level", "category"]
        
    def to_representation(self, instance: CoursesModel) -> Dict[str, str]:
        representation = super().to_representation(instance)
        
        profile = UserProfile.objects.get(owner=instance.owner.id)
        representation.update({
            "owner": {"id": instance.owner.id, "email": instance.owner.email},
            "owner_profile": {"profile_id": profile.id, "profile_username": profile.username},
            "category": {"id": instance.category.id, "category": instance.category.category},
            "rating": instance.ratingmodel_set.all().aggregate(Avg("rating"))["rating__avg"]
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
        
        profile = UserProfile.objects.get(owner=instance.owner)
        courses_item = CourseItemModel.objects.filter(course=instance.id)
        recommendations = CoursesModel.objects.filter(category=instance.category)
        recommendation_data = [{
            "id": recommended_course.id,
            "owner": profile.username,
            "title": recommended_course.title,
            "level": recommended_course.level,
            "preview_image": "http://localhost:8000/" + recommended_course.preview_image.url,
            "rating": instance.ratingmodel_set.all().aggregate(Avg("rating"))["rating__avg"],
            "category": {
                "id": recommended_course.category.id,
                "category": recommended_course.category.category
                }
            } for recommended_course in recommendations if recommended_course.id != instance.id
            ]
            
        representation.update({
            "owner": profile.username,
            "created_at": instance.created_at.strftime("%d.%m.%Y"),
            "updated_at": instance.updated_at.strftime("%d.%m.%Y"),
            "category": {"id": instance.category.id, "category": instance.category.category},
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
        representation["course"] = {"id": instance.course.id, "name": instance.course.title}
        return representation