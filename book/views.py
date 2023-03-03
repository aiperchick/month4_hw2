from django.http import HttpResponse
from django.shortcuts import render, get_list_or_404, get_object_or_404
from book import models, forms
from django.views import generic


class BookShow(generic.ListView):
    template_name = 'book.html'
    queryset = models.Book.objects.all()

    def get_queryset(self):
        return models.Book.objects.all()


class BookShowDetailView(generic.DetailView):
    template_name = 'book.full.html'

    def get_object(self, **kwargs):
        book_id = self.kwargs.get('id')
        return get_object_or_404(models.Book, id=book_id)


class BookShowForms(generic.CreateView):
    template_name = 'add_bookshow.html'
    form_class = forms.BookForm
    queryset = models.Book.objects.all()
    success_url = '/add-books/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(BookShowForms, self).form_valid(form=form)


class UpdateBookShow(generic.UpdateView):
    template_name = 'update_bookshow.html'
    form_class = forms.BookForm
    success_url = '/books/'

    def get_object(self, **kwargs):
        show_id = self.kwargs.get('id')
        return get_object_or_404(models.Book, id=show_id)

    def form_valid(self, form):
        return super(UpdateBookShow, self).form_valid(form=form)


class DeleteBookShow(generic.DeleteView):
    template_name = 'delete_bookshow.html'
    success_url = '/books/'

    def get_object(self, **kwargs):
        show_id = self.kwargs.get('id')
        return get_object_or_404(models.Book, id=show_id)


# добавление рейтинга
class RatingView(generic.CreateView):
    template_name = 'book.full.html'
    form_class = forms.CommentForm
    queryset = models.RatingBook.objects.all()
    success_url = '/books/<int:id>/'

    def form_valid(self, form):
        return super(RatingView, self).form_valid(form=form)


# добавление отзыва
class CommentShowView(generic.CreateView):

    template_name = 'comment_add.html'
    form_class = forms.CommentForm
    queryset = models.RatingBook.objects.all()
    success_url = '/add-comment/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(CommentShowView, self).form_valid(form=form)

