from rest_framework import generics, permissions
from .models import Reply
from .serializers import ReplySerializer
from comments.models import Comment
from paws_and_snaps_api.permissions import IsOwnerOrReadOnly
from django.shortcuts import get_object_or_404


class ReplyList(generics.ListCreateAPIView):

    queryset = Reply.objects.all()
    serializer_class = ReplySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


    def perform_create(self,serializer):
        comment_id = self.kwargs['comment_id']
        if comment_id is not None:
            comment = get_object_or_404(Comment,pk=comment_id)
            serializer.save(owner=self.request.user, comment=comment)
        else:
            raise serializers.ValidationError("comment_id parameter is missing in URL")


class ReplyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reply.objects.all()
    serializer_class = ReplySerializer
    permission_classes = [IsOwnerOrReadOnly]