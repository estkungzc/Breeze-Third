from django.shortcuts import render

books = [
    {
        'isbn': '90003249',
        'title': 'Software Engineering',
        'published_date': 'August 27, 2018',
        'publisher_id': 'CoreyMS'
    },
    {
        'isbn': '12302049',
        'title': 'Nazi Zombie',
        'published_date': 'August 28, 2018',
        'publisher_id': 'Jokasie'
    },
    {
        'isbn': '32943929',
        'title': 'Oscar',
        'published_date': 'Febuary 18, 2020',
        'publisher_id': 'Smither'
    },
    {
        'isbn': '2391239',
        'title': 'Cat VS Dog',
        'published_date': 'October 1, 2012',
        'publisher_id': 'FooBar'
    },
]

def home(request):
    context = {
        'books': books,
        'title': 'Book'
    }
    return render(request, 'books/book.html', context)

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