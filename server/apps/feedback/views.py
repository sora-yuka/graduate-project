from rest_framework import status
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.decorators import api_view
from rest_framework.viewsets import ModelViewSet

from .serializers import SavedSerializer, CommentSerializer, LikeSerializer
from .models import SavedModel, CommentModel, LikeModel
from .permissions import IsFeedBackOwner, IsFeedBackOwnerOrReadOnly
from apps.courses.models import CoursesModel

# Create your views here.


class FeedbackMixin:
    def save_course(
        self, 
        request: Request, 
        pk: int = None, 
        *args, **kwargs
    ) -> Response:
        try:
            save_obj, _ = SavedModel.objects.get_or_create(owner=request.user, course_id=pk)
            save_obj.is_saved = not save_obj.is_saved
            save_obj.save()
            response = {"MESSAGE": "Saved successfully!", "STATUS": status.HTTP_201_CREATED}
            
            if not save_obj.is_saved:
                save_obj.delete()
                response = {"MESSAGE": "Removed from saved", "STATUS": status.HTTP_204_NO_CONTENT}
            return Response(response, status=response["STATUS"])
        except Exception as error:
            print("An error occured while saving: ", error)
            return Response("Something went wrong while saving courses")
    
    def get_saves(
        self,
        request: Request,
        pk: int = None,
        *args, **kwargs
    ) -> Response:
        try:
            saves = SavedModel.objects.filter(owner=request.user, is_saved=True)
            serializer = SavedSerializer(saves, many=True).data
            return Response(data=serializer, status=status.HTTP_200_OK)
        except Exception as error:
            print("An error occured while getting saved: ", error)
            return Response("Something went wrong while getting saves")


    def like_course(
        self,
        request: Request,
        pk: int = None,
        *args, **kwargs
    ) -> Response:
        try:
            like_obj, _ = LikeModel.objects.get_or_create(owner=request.user, course_id=pk)
            like_obj.like = not like_obj.like
            like_obj.save()
            response = {"MESSAGE": "Course liked successfully", "STATUS": status.HTTP_201_CREATED}
            
            if not like_obj.like:
                like_obj.delete()
                response = {"MESSAGE": "Course unliked", "STATUS": status.HTTP_204_NO_CONTENT}
            return Response(response, status=response["STATUS"])
        except Exception as error:
            print("An error occured while liking: ", error)
    
    def get_likes(
        self,
        request: Request,
        pk: int = None,
        *args, **kwargs
    ) -> Response:
        likes = LikeModel.objects.filter(owner=request.user, like=True, course_id=pk).count()
        # is_liked = LikeModel.objects.get(owner=request.user, like=True)
        # serializer = LikeSerializer(likes, many=True).data
        # return Response(data=serializer, status=status.HTTP_200_OK)
        return Response(likes)
    
    
class CommentModelViewSet(ModelViewSet):
    permission_classes = [IsFeedBackOwnerOrReadOnly]
    serializer_class = CommentSerializer
    queryset = CommentModel.objects.all()
    
    def perform_create(self, serializer: CommentSerializer) -> CommentSerializer:
        return serializer.save(owner=self.request.user)
