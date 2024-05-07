# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
#from django.db.models import Count
from rest_framework import generics, permissions
#from django_filters.rest_framework import DjangoFilterBackend
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
    queryset = Article.objects.all()

    def perform_create(self, serializer):
    # Set the owner field before saving the serializer
        serializer.save(owner=self.request.user)

class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve an article and edit or delete it if you own it.
    """
    serializer_class = ArticleSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Article.objects.all()