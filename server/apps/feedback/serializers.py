from typing import Dict
from rest_framework import serializers
from .models import RatingModel, SavedModel, CommentModel, LikeModel

from apps.courses.models import CoursesModel


class RatingSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = RatingModel
        fields = "__all__"
        
    def to_representation(self, instance: RatingModel) -> Dict[str, str]:
        representation = super().to_representation(instance)
        user = User.objects.get(id=representation["owner"])
        course = CoursesModel.objects.get(id=representation["course"])
        representation["owner"] = {"id": user.id, "email": user.email}
        representation["course"] = {"id": course.id, "name": course.title}
        return representation
        

class SavedSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = SavedModel
        fields = "__all__"
        
    def to_representation(self, instance: SavedModel) -> Dict[str, str]:
        representation = super().to_representation(instance)
        user = User.objects.get(id=representation["owner"])
        course = CoursesModel.objects.get(id=representation["course"])
        representation["owner"] = {"id": user.id, "email": user.email}
        representation["course"] = {"id": course.id, "name": course.title}
        return representation
        

class CommentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CommentModel
        fields = "__all__"
        
    def to_representation(self, instance: CommentModel) -> Dict[str, str]:
        representation = super().to_representation(instance)
        user = User.objects.get(id=representation["owner"])
        course = CoursesModel.objects.get(id=representation["course"])
        representation["owner"] = {"id": user.id, "email": user.email}
        representation["course"] = {"id": course.id, "name": course.title}
        return representation
        

class LikeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = LikeModel
        fields = "__all__"
        
    def to_representation(self, instance: LikeModel) -> Dict[str, str]:
        representation = super().to_representation(instance)
        user = User.objects.get(id=representation["owner"])
        comment = CommentModel.objects.get(id=representation["comment"])
        representation["owner"] = {"id": user.id, "email": user.email}
        representation["comment"] = {"id": comment.id, "comment": comment.comment[:20]}
        return representation