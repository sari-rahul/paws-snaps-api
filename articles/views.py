# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.db.models import Count
from rest_framework import generics, filters,permissions
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Internal:
from paws_and_snaps_api.permissions import IsOwnerOrReadOnly
from articles.models import Article
from .serializers import ArticleSerializer
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class ArticleList(generics.ListCreateAPIView):
    """
    A class for the article list to view all articles
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = ArticleSerializer
    queryset = Article.objects.annotate(
        comment_count =Count('comment',distinct=True)
    ).order_by('-created_at')

    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
    ]
    search_fields = [
        'owner__username',
        'title',
        'category',
    ]
    
    ordering_fields = [
        'comment_count',
    ]

    def perform_create(self, serializer):
    # Set the owner field before saving the serializer
        serializer.save(owner=self.request.user)

class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve an article and edit or delete it if you own it.
    """
    serializer_class = ArticleSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Article.objects.annotate(
        comment_count =Count('comment',distinct=True)
    ).order_by('-created_at')