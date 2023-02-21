from django.db import models


class Book(models.Model):
    GENRE = (
        ('HORROR', 'HORROR'),
        ('NOVEL', 'NOVEL'),
        ('FANTASY', 'FANTASY'),
        ('PSYCHOLOGY', 'PSYCHOLOGY'),
        ('RELIGION', 'RELIGION')
    )

    title = models.CharField('название книги', max_length=100, null=True)
    description = models.TextField('описание книги', null=True)
    image = models.ImageField(upload_to='', null=True)
    genre = models.CharField(max_length=100, choices=GENRE, null=True)
    video = models.URLField(null=True)
    price = models.PositiveIntegerField('цена', null=True)
    created_dates = models.DateTimeField(auto_now_add=True, null=True)
    updated_dates = models.DateTimeField(auto_now=True, null=True)


def __str__(self):
    return self.title
