from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator

from apps.courses.models import CoursesModel

# Create your models here.

User = get_user_model()
    
    
class SavedModel(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(CoursesModel, on_delete=models.CASCADE)
    is_saved = models.BooleanField(default=False)
    
    def __str__(self) -> str:
        return f"{self.owner} saved '{self.course.title}' course"


class CommentModel(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(CoursesModel, on_delete=models.CASCADE)
    comment = models.TextField(help_text="Users comment")
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return f"{self.owner} leaved comment under {self.course}"

    
class LikeModel(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.ForeignKey(CommentModel, on_delete=models.CASCADE)
    like = models.BooleanField(default=False)
    
    def __str__(self) -> str:
        return f"{self.owner} - liked {self.comment.owner}s comment"