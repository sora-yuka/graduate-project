from rest_framework import serializers

from .models import ForumModel, ForumAnswerModel


class ForumSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ForumModel
        fields = "__all__"
        
    def to_representation(self, instance: ForumModel) -> ForumModel:
        representation = super().to_representation(instance)
        representationx.update({
            "owner": {"id": instance.owner.id, "email": instance.owner.email},
            "answers": instance.forumanswermodel_set.all()
        })
        return representation
    

class ForumAnswerSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ForumAnswerModel
        fields = "__all__"
        
    def to_representation(self, instance: ForumAnswerModel) -> ForumAnswerModel:
        representation = super().to_representation(instance)
        representationx.update({
            "owner": {"id": instance.owner.id, "email": instance.owner.email},
            "forum": {"id": instance.forum.id, "name": instance.forum.title}
        })
        return representation