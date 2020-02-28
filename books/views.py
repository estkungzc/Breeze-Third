from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.core.paginator import Paginator
from .forms import BookForm
from books.models import Book, Publisher, Author
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

# books = [
#     {
#         'isbn': '90003249',
#         'title': 'Software Engineering',
#         'published_date': 'August 27, 2018',
#         'publisher_id': 'CoreyMS'
#     },
#     {
#         'isbn': '12302049',
#         'title': 'Nazi Zombie',
#         'published_date': 'August 28, 2018',
#         'publisher_id': 'Jokasie'
#     },
#     {
#         'isbn': '32943929',
#         'title': 'Oscar',
#         'published_date': 'Febuary 18, 2020',
#         'publisher_id': 'Smither'
#     },
#     {
#         'isbn': '2391239',
#         'title': 'Cat VS Dog',
#         'published_date': 'October 1, 2012',
#         'publisher_id': 'FooBar'
#     },
# ]

def book_list(request):
    title = 'Book'
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = BookForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('books/book_list.html')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = BookForm()
        books = Book.objects.all()
        p = Paginator(books, 5)
        print(books)
        context = {
            'books': p,
            'form': form,
            'title': title
        }
    return render(request, 'books/book_list.html', context)

class BookListView(ListView):
    model = Book
    template_name = 'books/book_list.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'books'
    ordering = ['title']
    paginate_by = 5

def author(request):
    context = {
        'books': books,
        'title': 'Author'
    }
    return render(request, 'books/author.html', context)

def publisher(request):
    context = {
        'books': books,
        'title': 'Publisher'
    }
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