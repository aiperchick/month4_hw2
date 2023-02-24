from . import views
from django.urls import path

urlpatterns = [
    path('books/', views.books, name='books'),
    path('details/<int:id>/', views.book_full_view, name='details'),
    path('books/<int:id>/update/', views.update_book_show, name='update'),
    path('books/<int:id>/delete/', views.delete_book_show, name='delete'),
    path('add_book/', views.book_show_form, name='create'),
]
