from django.db import models
from django.contrib.postgres.fields import ArrayField

class Post(models.Model):
    Title=models.CharField(max_length=50, unique=True)
    Content=models.TextField(max_length=250)
    Category=models.CharField(max_length=50)
    Image= models.ImageField(upload_to='images/')
    Tags=ArrayField(models.CharField(max_length=255))
    def __str__(self) :
        return self.Title

