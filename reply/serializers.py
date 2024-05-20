from rest_framework import serializers
from .models import Reply

class ReplySerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Reply
        fields = ['id','owner','comment','created_at',
                    'updated_at','content']