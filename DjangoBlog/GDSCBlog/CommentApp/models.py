from django.db import models
from BlogApp.models import Post
from django.utils import timezone
class Comment(models.Model):
    Content=models.TextField(max_length=250)
    Author=models.CharField(max_length=50)
    PublishedDate=models.DateTimeField(default=timezone.now)
    Post=models.ForeignKey(Post,  on_delete=models.CASCADE)
