from typing import Dict
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from rest_framework import serializers


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
            serializers.ValidationError("Password didn't match.")
        return attrs
    
    def create(self, validated_data: Dict[str, str]) -> User:
        user = User.objects.create_user(**validated_data)
        user.save()
        return user
    
    
class ForgotPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True, write_only=True)
    
    def validate_email(self, email: str) -> str:
        user = User.objects.get(email=email)
        user.create_verification_code()
        user.save()
        return email
    

class RecoverAccountSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True, write_only=True)
    new_password = serializers.CharField(min_length=6)
    new_password_confirm = serializers.CharField(min_length=6)
    
    def validate_password(self, attrs: Dict[str, str]) -> Dict[str, str]:
        password = attrs.get("new_password")
        password_confirm = attrs.pop("new_password_confirm")
        
        if password != password_confirm:
            serializers.ValidationError("Password didn't match.")
        return attrs
    
    def set_new_password(self) -> None:
        user = User.objects.get(email=self.validated_data["email"])
        user.password = make_password(self.validated_data["new_password"])
        user.verification_code = ""
        user.save()
        
        
# TODO: change password, resend verification link