from . import views
from django.urls import path

urlpatterns = [
    path('books/', views.books, name='books'),
    path('details/<int:id>/', views.book_full_view, name='details'),
]
