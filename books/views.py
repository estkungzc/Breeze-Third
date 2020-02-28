from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import BookForm
from books.models import Book, Publisher, Author
from django.contrib import messages

from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

def book(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = BookForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # form.save()
            isbn = form.cleaned_data.get('isbn')
            title = form.cleaned_data.get('title')
            messages.success(request, f'Book has been created! {title}')
            return redirect('book_list')
    else:
        form = BookForm()
        book_list = Book.objects.all()
        page = request.GET.get('page', 1)

        paginator = Paginator(book_list, 5)
        try:
            books = paginator.page(page)
        except PageNotAnInteger:
            books = paginator.page(1)
        except EmptyPage:
            books = paginator.page(paginator.num_pages)
        context = {
            'books': books,
            'title': 'Book',
            'form': form
        }
        print(context)
        return render(request, 'books/book_list.html', context)

def book_insert(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = BookForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            isbn = form.cleaned_data.get('isbn')
            title = form.cleaned_data.get('title')
            messages.success(request, f'Book has been created! {title}')
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
        elif not form.is_valid():
            messages.warning(request, f'Book hasn\'t been created!')
        return redirect('book_list')


def search_books (request):
    # a = Book.written.objects.all()
    global namekeyword
    if request.method == 'POST':
        try:
            keyword_b = request.POST['name']
            keyword_y = request.POST['year']
            namekeyword = Book.objects.filter(title__startswith = keyword_b.lower(),published_date__year = keyword_y)
            page = request.GET.get('page', 1)

            paginator = Paginator(namekeyword, 5)
            try:
                books_filter = paginator.page(page)
            except PageNotAnInteger:
                books_filter = paginator.page(1)
            except EmptyPage:
                books_filter = paginator.page(paginator.num_pages)
            context = {'books':books_filter, 'title': 'Book'}
            print('my filter',context)
            return  render(request,'books/book_list.html',context)
        except:
            namekeyword = Book.objects.filter(title__startswith = keyword_b.lower())
            page = request.GET.get('page', 1)

            paginator = Paginator(namekeyword, 5)
            try:
                books_filter = paginator.page(page)
            except PageNotAnInteger:
                books_filter = paginator.page(1)
            except EmptyPage:
                books_filter = paginator.page(paginator.num_pages)
            context = {'books':books_filter, 'title': 'Book'}
            print('my filter',context)
            return  render(request,'books/book_list.html',context)
    else:
        page = request.GET.get('page')

        paginator = Paginator(namekeyword, 5)
        try:
            books_filter = paginator.page(page)
        except PageNotAnInteger:
            books_filter = paginator.page(1)
        except EmptyPage:
            books_filter = paginator.page(paginator.num_pages)
        context = {'books':books_filter, 'title': 'Book'}
        print('my filter',context)
        return  render(request,'books/book_list.html',context)        

class BookListView(ListView):
    model = Book
    template_name = 'books/book_list.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'books'
    ordering = ['title']
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super(BookListView, self).get_context_data(**kwargs)
        context['form'] = BookForm()
        return context

    

def author(request):
    context = {
        'books': [],
        'title': 'Author'
    }
    return render(request, 'books/author.html', context)

def publisher(request):
    publisher_list = Publisher.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(publisher_list, 5)
    try:
        publishers = paginator.page(page)
    except PageNotAnInteger:
        publishers = paginator.page(1)
    except EmptyPage:
        publishers = paginator.page(paginator.num_pages)
    context = {
        'publishers': publishers,
        'title': 'Publisher'
    }
    print(context)
    return render(request, 'books/publisher.html', context)

def work_for(request):
    context = {
        'books': books,
        'title': 'Work for'
    }
    return render(request, 'books/work_for.html', context)

def written(request):
    context = {
        'books': books,
        'title': 'Written'
    }
    return render(request, 'books/written.html', context)