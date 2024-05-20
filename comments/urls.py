from django.urls import path
from .views import CommentList, CommentDetail, CommentApproval

urlpatterns = [
    path('comments/',CommentList.as_view()),
    path('comments/<int:pk>',CommentDetail.as_view()),
    path('comments/<int:pk>/approve/', CommentApproval.as_view(), name='comment-approve'),
]