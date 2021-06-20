
from django.urls import path

from books_app.books.views import create_book, index, update_book

urlpatterns = [
    path('', index, name='index'),
    path('create/', create_book, name='create book'),
    path('update/<int:pk>', update_book, name='update book'),

]
