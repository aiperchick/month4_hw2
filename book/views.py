from django.shortcuts import render
from book import models


def books(requst):
    book = models.Book.objects.all()
    return render(requst, 'books.html', {'book': book})
