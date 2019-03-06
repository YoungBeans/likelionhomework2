from django.db import models

# Create your models here.

class Post(models.Model):
    author = models.CharField(max_length=20, blank=True)
    title = models.CharField(max_length=20)
    content = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    password = models.CharField(max_length=15)