from rest_framework import status
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.decorators import api_view

from .serializers import SavedSerializer, CommentSerializer, LikeSerializer
from .models import SavedModel, CommentModel, LikeModel
from .permissions import IsFeedBackOwner
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
            print(error)
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
            print(error)
            return Response("Something went wrong while getting saves")
