from django.db import models


class DoramyClub(models.Model):
    name = models.CharField(max_length=100)
    series = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    status = models.CharField(max_length=100)

    def __str__(self):
        return self.name
