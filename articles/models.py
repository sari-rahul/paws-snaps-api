# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.db import models
from django.contrib.auth.models import User

class Article(models.Model):
    categories = [
        ('dogs','Dogs'),
        ('cats','Cats'),
        ('fishes','Fishes'),
        ('birds','Birds'),
        ('horses','Horses'),
        ('training','Training'),
        ('wellness','Wellness'),
        ('adoption','Adoption'),
        ('other', 'Other'),
    ]

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    article = models.TextField()
    category = models.CharField(
        max_length=250,
        blank=True,
        null=True,
        default='Other',
        choices=categories
    ) 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    image = models.ImageField(
        upload_to='images/',default='../default_post_elqjw1')
        
    published = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['-created_at']
    def __str__(self):
         return f'{self.id} {self.title}'

