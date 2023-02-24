from django.http import HttpResponse
from django.shortcuts import render, get_list_or_404, get_object_or_404
from book import models, forms


def books(requst):
    book = models.Book.objects.all()
    return render(requst, 'book.html', {'book': book})


def book_full_view(request, id):
    book_id = get_list_or_404(models.Book, id=id)
    return render(request, 'book.full.html', {'books_id': book_id})


# Добавление книг через формы
def book_show_form(request):
    method = request.method
    if method == 'POST':
        form = forms.BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('<h2>книга добавлена</h2>')

    else:
        form = forms.BookForm()

    return render(request, 'add_bookshow.html', {'form': form})


# изменение данных о книге
def update_book_show(request, id):
    show_object = get_object_or_404(models.Book, id=id)
    if request.method == 'POST':
        form = forms.BookForm(instance=show_object, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('<h2>Книга успешно обновлена!</h2>')
    else:
        form = forms.BookForm(instance=show_object)

    return render(request, 'update_bookshow.html', {
                                                    'form': form,
                                                    'object': show_object
                                                   })


# Удаление из базы
def delete_book_show(request, id):
    show_object = get_object_or_404(models.Book, id=id)
    show_object.delete()
    return HttpResponse('<h2>Книга удалена</h2>')

