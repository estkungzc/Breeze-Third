from django.urls import path
from .views import (
    BookListView,
)
from . import views

app_name='books'

urlpatterns = [
    path('', views.book, name='book-list'),
    path('author', views.author, name='book-author'),
    path('publisher', views.publisher, name='book-publisher'),
    path('work-for', views.work_for, name='book-workfor'),
    path('written', views.written, name='book-written'),
    path('search', views.search_books, name='search'),
    path('post', views.book_insert, name='book-post'),
]