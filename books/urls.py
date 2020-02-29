from django.urls import path
from . import views
from .views import (
    BookUpdateView,
)
app_name='books'

urlpatterns = [
    path('', views.home, name='home'),
    path('book', views.book, name='book'),
    path('author', views.author, name='author'),
    path('publisher', views.publisher, name='publisher'),
    path('search-book', views.search_books, name='search-book'),
    path('search-author', views.search_author, name='search-author'),
    path('search-publisher', views.search_publisher, name='search-publisher'),
    path('<str:state>/insert/', views.insert, name='insert'),
    path('<str:state>/<str:m_pk>/edit', views.edit, name='edit'),
    path('<str:state>/<str:m_pk>/delete_data/', views.delete, name='delete_data'),
]