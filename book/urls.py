from . import views
from django.urls import path

urlpatterns = [
    path('books/', views.BookShow.as_view(), name='books'),
    path('books/<int:id>/', views.BookShowDetailView.as_view(), name='details'),
    path('books/<int:id>/change/', views.UpdateBookShow.as_view(), name='update'),
    path('books/<int:id>/delete/', views.DeleteBookShow.as_view(), name='delete'),
    path('add-books/', views.BookShowForms.as_view(), name='create'),
    path('add-comment/', views.CommentShowView.as_view(), name='comment'),
]
