from django.shortcuts import render
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from .serializers import RatingSerializer, SavedSerializer, CommentSerializer, LikeSerializer
from .models import RatingModel, SavedModel, CommentModel, LikeModel

# Create your views here.


class SavedViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin, 
    mixins.DestroyModelMixin, 
    GenericViewSet
):
    permission_classes = []
    serializer_class = SavedSerializer
    queryset = SavedModel.objects.all()
    
    def perform_create(self, serializer: SavedSerializer) -> SavedSerializer:
        return serializer.save(owner=self.request.user)
