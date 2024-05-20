from django.db import models
from django.contrib.auth.models import User
from comments.models import Comment

class Reply(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE ,related_name='replies')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now=True)
    content = models.TextField()


    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        
        return f"Reply by {self.owner.username} to {self.comment}"