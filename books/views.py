from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import BookForm, AuthorForm, PublisherForm
from books.models import Book, Publisher, Author
from django.contrib import messages

from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

def home(request):
    context = {
        'title': 'Home',
    }
    return render(request, 'books/book_home.html', context)

def book(request):
    form = BookForm()
    book_list = Book.objects.all()
    books = _get_object_paginator(request, book_list)

    context = {
        'books': books,
        'title': 'Book',
        'form': form
    }
    return render(request, 'books/book_list.html', context)


def insert(request, state):
    if request.method != 'POST':
        return redirect(f'/{state}')

    if state == "book":
        form = BookForm(request.POST)
    elif state == "author":
        form = AuthorForm(request.POST)
    elif state == "publisher":
        form = PublisherForm(request.POST)
    
    if form.is_valid():
        form.save()
        messages.success(request, 'Insert Success')
    else:
        messages.warning(request, 'Insert Error')
    return redirect(f'/{state}')
class BookUpdateView(UpdateView):
    model = Book
    fields = '__all__'

    def form_valid(self, form):
        clean = form.cleaned_data 
        context = {}        
        self.object = context.save(clean) 
        return super(BookUpdateView, self).form_valid(form)


def _get_object_paginator(request, obj_list):
    page = request.GET.get('page', 1)

    paginator = Paginator(obj_list, 5)
    try:
        return paginator.page(page)
    except PageNotAnInteger:
        return paginator.page(1)
    except EmptyPage:
        return paginator.page(paginator.num_pages)

def search_books (request):
    # a = Book.written.objects.all()
    global book_qs
    form = BookForm()
    if request.method == 'POST':
        book_qs = Book.objects.all().order_by('title')
        book_name = request.POST['book_name']
        publisher_name = request.POST['publisher_name']
        year = request.POST['year']
        if(book_name != '' and book_name != None):
            # print(f'Hey i want to see book name: {book_name}')
            book_qs = book_qs.filter(title__istartswith = book_name)
        if(publisher_name != '' and publisher_name != None):
            # print(f'I want to know publisher name: {publisher_name}')
            book_qs = book_qs.filter(publisher__name__istartswith = publisher_name)
        if(year != '' and year != None):
            # print(f'I want to know year: {year}')
            book_qs = book_qs.filter(published_date__year = year)
        book_pageobj = _get_object_paginator(request, book_qs)
        context = {
            'books':book_pageobj, 
            'title': 'Book',
            'form': form
        }
        return  render(request,'books/book_list.html', context)
    else:
        book_pageobj = _get_object_paginator(request, book_qs)
        context = {
            'books':book_pageobj, 
            'title': 'Book',
            'form': form    
        }
        return  render(request,'books/book_list.html',context)        

def author(request):
    form = AuthorForm()
    author_list = Author.objects.all()
    authors = _get_object_paginator(request, author_list)
    context = {
        'authors': authors,
        'title': 'Author',
        'form': form
    }
    print(context)
    return render(request, 'books/author_list.html', context)

def search_author (request):
    global author_keyword
    form = AuthorForm()
    if request.method == 'POST':
        keyword_a = request.POST['name']
        author_keyword = Author.objects.filter(author_name__startswith = keyword_a.capitalize())
        authors_filter = _get_object_paginator(request, author_keyword)
        context = {
            'authors':authors_filter,
            'title': 'Author',
            'form': form
        }
    else:
        authors_filter = _get_object_paginator(request, author_keyword)
        context = {
            'authors':authors_filter, 
            'title': 'Author',
            'form': form    
        }
    return  render(request,'books/author_list.html',context)


def publisher(request):
    form = PublisherForm()
    publisher_list = Publisher.objects.all()
    publishers = _get_object_paginator(request, publisher_list)
    context = {
        'publishers': publishers,
        'title': 'Publisher',
        'form': form
    }
    return render(request, 'books/publisher_list.html', context)

def search_publisher (request):
    global publisher_keyword
    form = PublisherForm()
    if request.method == 'POST':
        keyword_a = request.POST['name']
        publisher_keyword = Publisher.objects.filter(name__startswith = keyword_a.capitalize())
        publishers_filter = _get_object_paginator(request, publisher_keyword)
        context = {
            'publishers':publishers_filter,
            'title': 'Publisher',
            'form': form
        }
    else:
        publishers_filter = _get_object_paginator(request, publisher_keyword)
        context = {
            'publishers':publishers_filter, 
            'title': 'Publisher',
            'form': form    
        }
    return  render(request,'books/publisher_list.html',context)    