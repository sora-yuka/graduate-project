from typing import Dict
from rest_framework import serializers
from django.contrib.auth import get_user_model

from apps.courses.models import CoursesModel
from apps.profiles.models import UserProfile
from .models import SavedModel, CommentModel, LikeModel

User = get_user_model()


class SavedSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = SavedModel
        exclude = ["owner"]
        
    def to_representation(self, instance: SavedModel) -> Dict[str, str]:
        representation = super().to_representation(instance)
        
        representation.update({
            "course": {"id": instance.course.id, "name": instance.course.title},
            "preview_image": "http://localhost:8000" + instance.course.preview_image.url
        })
        return representation
        

class CommentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CommentModel
        exclude = ["owner"]
        
    def to_representation(self, instance: CommentModel) -> Dict[str, str]:
        representation = super().to_representation(instance)
        course = CoursesModel.objects.get(id=instance.course.id)
        profile = UserProfile.objects.get(owner=instance.owner)
        representation.update({
            "id": instance.id,
            "owner": {"id": instance.owner.id, "email": instance.owner.email},
            "username": profile.username,
            "course": {"id": course.id, "name": course.title},
            "created_at": instance.created_at.strftime("%d.%m.%Y")
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