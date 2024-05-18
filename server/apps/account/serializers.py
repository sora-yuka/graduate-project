from typing import Dict
from rest_framework import serializers
from django.contrib.auth import get_user_model


User = get_user_model()


class UserRegisterSerializer(serializers.ModelSerializer):
    password_confirm = serializers.CharField(
        required=True, 
        min_length=6, 
        write_only=True
        )
    
    class Meta:
        model = User
        fields = [
            "id",
            "email",
            "password",
            "password_confirm",
        ]
        
    def validate(self, attrs: Dict[str, str]) -> Dict[str, str]:
        password = attrs.get("password")
        password_confirm = attrs.pop("password_confirm")
        
        if password != password_confirm:
            serializers.ValidationError("Password didn't match")
        return attrs
    
    def create(self, validated_data: Dict[str, str]) -> User:
        user = User.objects.create_user(**validated_data)
        user.save()
        return user