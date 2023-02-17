from . import views
from django.urls import path

urlpatterns = [
    path('book/', views.books, name='books'),
    path('book/<int:id>/', views.book_full_view, name='details'),
]
