from typing import Dict
from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import UserProfile


User = get_user_model()


class UserProfileSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = UserProfile
        fields = "__all__"
        
    def to_representation(self, instance: UserProfile) -> Dict[str, str | int]:
        representation = super().to_representation(instance)
        user = User.objects.get(id=instance.owner.id)
        representation["owner"] = {"id": user.id, "email": user.email}
        return representation