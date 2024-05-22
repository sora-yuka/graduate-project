from django.contrib import admin
from .models import RatingModel, CommentModel, LikeModel, SavedModel

# Register your models here.


admin.site.register(RatingModel)
admin.site.register(CommentModel)
admin.site.register(LikeModel)
admin.site.register(SavedModel)