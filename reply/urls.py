from django.urls import path
from .views import ReplyList, ReplyDetail

urlpatterns= [
    path('comments/<int:comment_id>/replies/',ReplyList.as_view(),name='rely_list'),
    path('comments/<int:comment_id>/replies/<int:pk>',ReplyDetail.as_view(),name='rely_detail'),    
    ]