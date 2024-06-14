from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet, ModelViewSet
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.decorators import api_view
from django_filters.rest_framework import DjangoFilterBackend

from .models import CoursesModel, CourseItemModel, CategoryModel
from .serializers import AllCoursesSerialier, CategorySerializer, DetailedCourseSerializer, CourseItemSerializer
from .permissions import IsCourseOwner
from apps.profiles.models import UserProfile
from apps.feedback.views import FeedbackMixin

# Create your views here.


class CoursePagination(PageNumberPagination):
    page_size = 9
    max_page_size = 100
    page_size_query_param = "courses"


class AllCourseViewSet(mixins.ListModelMixin, GenericViewSet):
    serializer_class = AllCoursesSerialier
    queryset = CoursesModel.objects.order_by("-updated_at").distinct()
    
    
    pagination_class = CoursePagination
    filter_backends = [SearchFilter, OrderingFilter, DjangoFilterBackend]
    filterset_fields = ["category", "level"]
    search_fields = ["title"]
    ordering_fields = ["created_at"]


class LatestCourseViewSet(mixins.ListModelMixin, GenericViewSet):
    serializer_class = AllCoursesSerialier
    queryset = CoursesModel.objects.order_by("-created_at")[:4]

    
class CourseViewSet(
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    GenericViewSet,
    FeedbackMixin
):
    permission_classes = [IsCourseOwner]
    serializer_class = DetailedCourseSerializer
    queryset = CoursesModel.objects.all()
    
    def perform_create(self, serializer: DetailedCourseSerializer) -> DetailedCourseSerializer:
        return serializer.save(owner=self.request.user)
    
    def get_queryset(self):
        return super().get_queryset()
    
    
class CourseItemViewSet(ModelViewSet):
    permission_classes = [IsCourseOwner]
    serializer_class = CourseItemSerializer
    queryset = CourseItemModel.objects.all()
    
    def perform_create(self, serializer: CourseItemSerializer) -> CourseItemSerializer:
        return serializer.save(owner=self.request.user)
    
    def get_queryset(self) -> CourseItemModel:
        course = self.kwargs["course_pk"]
        return CourseItemModel.objects.filter(course=course)