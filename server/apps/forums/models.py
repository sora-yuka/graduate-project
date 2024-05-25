from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.

User = get_user_model()


class ForumModel(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    question_preview = models.ImageField(upload_to="forum/")
    question_text = models.TextField(help_text="Users issue explaining")
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return f"{self.owner.email} - {self.title}"
    

class ForumAnswerModel(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    forum = models.ForeignKey(ForumModel, on_delete=models.CASCADE)
    answer = models.TextField(help_text="Users answer on forum")
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return f"{self.owner.email} {self.forum.title}"