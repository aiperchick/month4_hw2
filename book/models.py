from django.db import models

class Book(models.Model):
    titles = models.CharField(max_length=100)
    descriptions = models.TextField()
    images = models.ImageField(upload_to='')
    created_dates = models.DateTimeField(auto_now_add=True)
    updated_dates = models.DateTimeField(auto_now=True)
