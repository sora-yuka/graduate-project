from typing import Dict
from rest_framework import serializers
from django.contrib.auth import get_user_model

from .models import CoursesModel, CourseItemModel

User = get_user_model()


class AllCoursesSerialier(serializers.ModelSerializer):
    
    class Meta:
        model = CoursesModel
        fields = ["id", "owner", "title", "preview_image"]
        
