from django.db import models
from django.utils import timezone
  # Create your models here.

class comment(models.Model):
    content=models.TextField()
    feedback=models.CharField(max_length=250)
    Created_time=models.DateTimeField(default=timezone.now)
    updated=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.content
# class classex(models.Model):
#     name=models.CharField(max_length=255)
#     age=models.IntegerField()
#     price=models.FloatField()
#     result=models.FloatField()
#     def __str__(self):
#         return self.result


class Author(models.Model):
    name = models.CharField(max_length=100)
class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publication_date = models.DateField(auto_now_add=True)

# Creating a new record
author = Author.objects.create(name='Jane Smith')
blog_post = BlogPost.objects.create(title='Django for Beginners', content='Lorem ipsum...', author=author)
