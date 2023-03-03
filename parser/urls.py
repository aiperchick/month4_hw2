from django.urls import path
from . import views

app_name = 'parse'
urlpatterns = [
    path('doramy_list/', views.ParserView.as_view(), name='doramy_list'),
    path('parsing/', views.ParserForm.as_view(), name='parser_doramy'),
]