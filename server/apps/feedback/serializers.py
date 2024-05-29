from typing import Dict
from rest_framework import serializers
from django.contrib.auth import get_user_model
from apps.courses.models import CoursesModel
from .models import RatingModel, SavedModel, CommentModel, LikeModel

User = get_user_model()


class RatingSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = RatingModel
        exclude = ["owner"]
        

class SavedSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = SavedModel
        exclude = ["owner"]
        
    def to_representation(self, instance: SavedModel) -> Dict[str, str]:
        representation = super().to_representation(instance)
        
        representation.update({
            "course": {"id": instance.course.id, "name": instance.course.title},
        })
        return representation
        

class CommentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CommentModel
        fields = "__all__"
        
    def to_representation(self, instance: CommentModel) -> Dict[str, str]:
        representation = super().to_representation(instance)
        course = CoursesModel.objects.get(id=instance.course.id)
        representation.update({
            "owner": {"id": instance.owner.id, "email": instance.owner.email},
            "course": {"id": course.id, "name": course.title}
        })
        return representation
        

class LikeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = LikeModel
        fields = "__all__"
        
    def to_representation(self, instance: LikeModel) -> Dict[str, str]:
        representation = super().to_representation(instance)
        comment = CommentModel.objects.get(id=instance.comment.id)
        representation.update({
            "owner": {"id": instance.owner.id, "email": instance.owner.email},
            "comment": {"id": comment.id, "comment": comment.comment[:20]}
        })
        return representation