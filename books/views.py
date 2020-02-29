from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import BookForm, AuthorForm, PublisherForm
from books.models import Book, Publisher, Author
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import MySQLdb

db = MySQLdb.connect(host="mybookdatabase.mariadb.database.azure.com",    # your host, usually localhost
                     user="admin_mnk@mybookdatabase",         # your username
                     passwd="#Patt1994",  # your password
                     db="bookdb")        # name of the data base
cur = db.cursor()

from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

def home(request):
    context = {
        'state': 'home',
    }
    return render(request, 'books/book_home.html', context)

def book(request):
    form = BookForm()
    book_list = Book.objects.all()
    books = _get_object_paginator(request, book_list)
    fields_book = Book._meta.get_fields()
    # print(fields_book)
    context = {
        'books': books,
        'fields': fields_book,
        'state': 'book',
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
            'state': 'book',
            'form': form
        }
        return  render(request,'books/book_list.html', context)
    else:
        book_pageobj = _get_object_paginator(request, book_qs)
        context = {
            'books':book_pageobj, 
            'state': 'book',
            'form': form    
        }
        return  render(request,'books/book_list.html',context)        

def author(request):
    form = AuthorForm()
    author_list = Author.objects.all()
    authors = _get_object_paginator(request, author_list)
    context = {
        'authors': authors,
        'state': 'author',
        'form': form
    }
    # print(context)
    return render(request, 'books/author_list.html', context)

def search_author (request):
    global author_keyword
    form = AuthorForm()
    if request.method == 'POST':
        keyword_a = request.POST['name']
        author_keyword = Author.objects.filter(author_name__istartswith = keyword_a)
        authors_filter = _get_object_paginator(request, author_keyword)
        context = {
            'authors':authors_filter,
            'state': 'author',
            'form': form
        }
    else:
        authors_filter = _get_object_paginator(request, author_keyword)
        context = {
            'authors':authors_filter, 
            'state': 'author',
            'form': form    
        }
    return  render(request,'books/author_list.html',context)


def publisher(request):
    form = PublisherForm()
    publisher_list = Publisher.objects.all()
    publishers = _get_object_paginator(request, publisher_list)
    context = {
        'publishers': publishers,
        'state': 'publisher',
        'form': form
    }
    return render(request, 'books/publisher_list.html', context)

def search_publisher (request):
    global publisher_keyword
    form = PublisherForm()
    if request.method == 'POST':
        keyword_a = request.POST['name']
        publisher_keyword = Publisher.objects.filter(name__istartswith = keyword_a)
        publishers_filter = _get_object_paginator(request, publisher_keyword)
        context = {
            'publishers':publishers_filter,
            'state': 'publisher',
            'form': form
        }
    else:
        publishers_filter = _get_object_paginator(request, publisher_keyword)
        context = {
            'publishers':publishers_filter, 
            'state': 'publisher',
            'form': form    
        }
    return  render(request,'books/publisher_list.html',context)

def delete(request,state,m_pk):
    if state=="book":
        data = Book.objects.get(isbn=m_pk)
    elif state=="author":
        data = Author.objects.get(author_name=m_pk)
    elif state=="publisher":   
        data = Publisher.objects.get(name=m_pk)
    data.delete()
    messages.success(request, f'Delete {state.capitalize()} Success')
    return HttpResponseRedirect(reverse(f'books:{state}'))

def edit(request,state,m_pk):
    if state=="book":
        if request.method == 'POST':
            try :
                data = Book.objects.get(isbn=m_pk)
                data.isbn = request.POST['isbn']
                data.title = request.POST['title']
                data.published_date = request.POST['published_date']
                data.publisher= Publisher.objects.get(name=request.POST['publisher'])
                data.save()
                messages.success(request, 'Edit Success')
            except:
                messages.warning(request, 'Edit Error')

        fields_book = Book._meta.get_fields()[:3]
        d_book = Book.objects.get(isbn = m_pk )
        d_book_list = Book.objects.values_list().get(isbn = m_pk )
        p_pk = Publisher.objects.all()
        a_pk = Author.objects.all()
        mylist = zip(fields_book,d_book_list)
        context = {"state":"book","mylist":mylist,"pk":m_pk,"d_book":d_book.publisher.name,"publisher_name":p_pk,"a_name":a_pk}
                
    elif state=="author":
        if request.method == 'POST':
            try :
                data = Author.objects.get(author_name=m_pk)
                data.author_name = request.POST['author_name']
                data.date_of_birth = request.POST['date_of_birth']
                data.save()
                messages.success(request, 'Edit Success')
            except:
                messages.warning(request, 'Edit Error')
        p_pk = Publisher.objects.all()
        d_author_list = Author.objects.values_list().get(author_name = m_pk )
        d_author = Author.objects.get(author_name = m_pk )
        fields_author = Author._meta.get_fields()[1:3]
        mylist = zip(fields_author,d_author_list)
        context = {"state":"author","mylist":mylist,"pk":m_pk,"publisher_name":p_pk}

    elif state=="publisher":
        if request.method == 'POST':
            try :
                data = Publisher.objects.get(name=m_pk) 
                data.name = request.POST['name']
                data.address=request.POST['address']
                data.phone=request.POST['phone']
                data.save()
                messages.success(request, 'Edit Success')
            except:
                messages.warning(request, 'Edit Error')
        d_publisher = Publisher.objects.values_list().get(name = m_pk )
        fields_publisher = Publisher._meta.get_fields()[2:]
        mylist = zip(fields_publisher,d_publisher)
        context = {"state":"publisher","f_model":fields_publisher,"model_d":d_publisher,"mylist":mylist,"pk":m_pk}
    return render(request, 'books/edit.html',context)

@login_required
def query(request):
    if request.method == 'POST':
        try:
            test_sql=request.POST['sql_code']
            print(test_sql)
        except (KeyError):
            return render(request, 'books/query.html')
        else:
            try:
                cur.execute(test_sql)
            except:
                context = {'state':'query', 'code':test_sql,'error':'Query not found'}
                return render(request, 'books/query.html',context)
            else:
                desc = cur.description
                query_list = cur.fetchall()
                print(query_list)
                context = {'state':'query', 'query': query_list,'code':test_sql,'len_query':len(query_list),'desc':desc}
                return render(request, 'books/query.html',context)
    return render(request, 'books/query.html', {'state': 'query'})