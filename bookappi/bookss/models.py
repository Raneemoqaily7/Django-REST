from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.deletion import CASCADE



class Book (models.Model):
    title = models.CharField(max_length=64)
    reviewer =models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    timestamp =models.DateTimeField(auto_now_add=True)
    updatedtime =models.DateTimeField(auto_now=True )
    description =models.TextField()



    def __str__(self):
        return self.title




