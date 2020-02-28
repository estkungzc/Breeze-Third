from django.urls import path
from .views import (
    BookListView,
)
from . import views

urlpatterns = [
    path('', views.BookListView.as_view(), name='book-list'),
    path('author', views.author, name='book-author'),
    path('publisher', views.publisher, name='book-publisher'),
    path('work-for', views.work_for, name='book-workfor'),
    path('written', views.written, name='book-written')
]