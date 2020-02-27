from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='book-home'),
    path('author', views.author, name='book-author'),
    path('publisher', views.publisher, name='book-publisher'),
    path('work-for', views.work_for, name='book-workfor'),
    path('written', views.written, name='book-written')
]