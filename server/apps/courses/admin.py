from django.contrib import admin
from .models import CoursesModel, CourseItem

# Register your models here.

admin.site.register(CoursesModel)
admin.site.register(CourseItem)