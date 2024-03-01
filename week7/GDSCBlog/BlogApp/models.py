from django.db import models

class Postt(models.Model):
    Title=models.CharField(max_length=50, unique=True)
    Content=models.TextField(max_length=250)
    Category=models.CharField(max_length=50)
    Image= models.ImageField()

    def __str__(self) :
        return self.Title

