# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.contrib.humanize.templatetags.humanize import naturaltime
from rest_framework import serializers
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Internal:
from .models import Comment
from likes.models import Like

class CommentSerializer(serializers.ModelSerializer):
    """
    A class for the comment serializer
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()
    like_id = serializers.SerializerMethodField()
    likes_count = serializers.ReadOnlyField()

    class Meta:
        model = Comment
        fields = [
            'id',
            'owner',
            'is_owner',
            'profile_id',
            'profile_image',
            'article', 
            'created_at',
            'updated_at',
            'content',
            'like_id',
            'likes_count',
            'is_approved',
        ]

    def get_created_at(self, obj):
        """
        Will return a formatted date to indicate when the comment was created
        """
        return naturaltime(obj.created_at)

    def get_updated_at(self, obj):
        """
        Will return a formatted date to indicate when the comment was updated
        """
        return naturaltime(obj.updated_at)

    # Returns True if the current user is the owner of the comment
    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_like_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            like = Like.objects.filter(
                owner=user, comment=obj
            ).first()
            return like.id if like else None
        return None


class CommentDetailSerializer(CommentSerializer):
    """
    A class for the comment detail serializer
    That inherits from the comment serializer
    """
    article = serializers.ReadOnlyField(source='article.id')
    is_approved = serializers.BooleanField(read_only=True)  


class CommentApprovalSerializer(serializers.ModelSerializer):
    """
    Serializer for comment approval
    """
    is_approved = serializers.BooleanField(required=False) 
    content = serializers.CharField(read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'content', 'is_approved'] 

    def to_representation(self, instance):
        """
        Serialize the instance, including the content field and a default value for is_approved
        """
        data = super().to_representation(instance)
        data['is_approved'] = False  # Default value for approval checkbox
        return data