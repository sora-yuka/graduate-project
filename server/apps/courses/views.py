from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView

from .models import CoursesModel, CourseItemModel
from .serializers import AllCoursesSerialier

# Create your views here.


class AllCoursesListAPIView(ListAPIView):
    serializer_class = AllCoursesSerialier
    queryset = CoursesModel.objects.all()