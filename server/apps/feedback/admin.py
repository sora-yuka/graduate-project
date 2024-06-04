from django.contrib import admin
from .models import CommentModel, LikeModel, SavedModel

# Register your models here.


admin.site.register(CommentModel)
admin.site.register(LikeModel)
admin.site.register(SavedModel)