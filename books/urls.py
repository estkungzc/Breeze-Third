from django.urls import path
from . import views
from .views import (
    BookUpdateView,
)
app_name='books'

urlpatterns = [
    path('', views.book, name='book-list'),
    path('book/<str:pk>/update/', BookUpdateView.as_view(), name='post-update'),
    path('author', views.author, name='book-author'),
    path('publisher', views.publisher, name='book-publisher'),
    path('search-book', views.search_books, name='search-book'),
    path('search-author', views.search_author, name='search-author'),
    path('search-publisher', views.search_publisher, name='search-publisher'),
]