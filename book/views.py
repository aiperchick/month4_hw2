from django.shortcuts import render, get_list_or_404
from book import models


def books(requst):
    book = models.Book.objects.all()
    return render(requst, 'book.html', {'book': book})


def book_full_view(request, id):
    book_id = get_list_or_404(models.Book, id=id)
    return render(request, 'book.full.html', {'books_id': book_id})
