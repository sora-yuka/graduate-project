from django.shortcuts import render
from rest_framework import mixins
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import ForumModel, ForumAnswerModel
from .serializers import ForumSerializer, ForumAnswerSerializer

# Create your views here.


class ForumViewSet(ModelViewSet):
    serializer_class = ForumSerializer
    queryset = ForumModel.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def perform_create(self, serializer: ForumSerializer) -> ForumSerializer:
        return serializer.save(owner=self.request.user)
    

class ForumAnswerViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    GenericViewSet
):
    serializer_class = ForumAnswerSerializer
    queryset = ForumAnswerModel.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def perform_create(self, serializer: ForumAnswerSerializer) -> ForumAnswerSerializer:
        return serializer.save(owner=self.request.user)