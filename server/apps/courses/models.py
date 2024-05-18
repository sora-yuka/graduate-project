from django.db import models
from django.contrib.auth import get_user_model
from ext.choices import LEVEL

# Create your models here.

User = get_user_model()

# TODO: CREATE CATEGORY MODEL


class CoursesModel(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    level = models.CharField(max_length=100, choices=LEVEL)
    preview_image = models.ImageField(upload_to="preview/images/")
    preview_video = models.FileField(upload_to="preview/videos/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.title
    

class CourseItem(models.Model):
    course_id = models.ForeignKey(CoursesModel, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    file = models.FileField(upload_to="course/")
    description = models.TextField(blank=True, null=True)
    
    def __str__(self) -> str:
        return self.name