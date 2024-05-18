from rest_framework import serializers

from .models import CoursesModel, CourseItem


class CourseSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CoursesModel
        fields = "__all__"