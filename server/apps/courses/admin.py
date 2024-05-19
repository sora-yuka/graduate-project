from django.contrib import admin
from .models import CoursesModel, CourseItemModel

# Register your models here.

admin.site.register(CoursesModel)
admin.site.register(CourseItemModel)