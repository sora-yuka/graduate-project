from django.shortcuts import render
from rest_framework.generics import ListAPIView

from .models import CoursesModel
from .serializers import CourseSerializer

# Create your views here.


class CourseView(ListAPIView):
    serializer_class = CourseSerializer
    queryset = CoursesModel.objects.all()