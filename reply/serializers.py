from rest_framework import serializers
from .models import Reply
from comments.models import Comment

class ReplySerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    comment_id = serializers.PrimaryKeyRelatedField(queryset=Comment.objects.all(), source='comment', write_only=True)
    class Meta:
        model = Reply
        fields = ['id','owner','comment_id','created_at',
                    'updated_at','content']