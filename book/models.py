from django.db import models


class Book(models.Model):
    GENRE = (
        ('HORROR', 'HORROR'),
        ('NOVEL', 'NOVEL'),
        ('FANTASY', 'FANTASY'),
        ('PSYCHOLOGY', 'PSYCHOLOGY'),
        ('RELIGION', 'RELIGION')
    )

    title = models.CharField('название книги', max_length=100)
    description = models.TextField('описание книги')
    image = models.ImageField(upload_to='')
    genre = models.CharField(max_length=100, choices=GENRE)
    video = models.URLField()
    price = models.PositiveIntegerField('цена', null=True)
    created_dates = models.DateTimeField(auto_now_add=True, null=True)
    updated_dates = models.DateTimeField(auto_now=True, null=True)


def __str__(self):
    return self.title
