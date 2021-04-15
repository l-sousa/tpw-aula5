from django.http import HttpResponse
from django.shortcuts import render, redirect
from app.forms import *
from app.models import Book, Author, Publisher


# Create your views here.


def default(request):
    return render(request, 'default.html')


def books(request):
    tparams = {
        'books': Book.objects.all()
    }
    return render(request, 'books.html', tparams)


def book_details(request, book_name):
    tparams = {
        'book': Book.objects.get(title=book_name)
    }
    return render(request, 'book_detalis.html', tparams)


def authors(request):
    tparams = {
        'authors': Author.objects.all()
    }
    return render(request, 'authors.html', tparams)


def author_details(request, author_name):
    tparams = {
        'author': Author.objects.get(name=author_name)
    }
    return render(request, 'author_details.html', tparams)


def publishers(request):
    tparams = {
        'publishers': Publisher.objects.all()
    }
    return render(request, 'publishers.html', tparams)


def publisher_details(request, publisher_name):
    tparams = {
        'publisher': Publisher.objects.get(name=publisher_name)
    }
    return render(request, 'publisher_details.html', tparams)


def author_books(request, author_name):
    tparams = {
        'books': Book.objects.filter(authors__name__contains=author_name),
        'author_name': author_name
    }
    return render(request, 'author_books.html', tparams)


def publisher_authors(request, publisher_name):
    tparams = {
        'books_of_publisher': Book.objects.filter(publisher__name__contains=publisher_name),
        'pub_name': publisher_name
    }
    return render(request, 'publisher_authors.html', tparams)


def booksearch(request):
    if 'query' in request.POST:
        query = request.POST['query']
        if query:
            books = Book.objects.filter(title__icontains=query)
            return render(request, "booklist.html", {'books': books, 'query': query})
        else:
            return render(request, "booksearch.html", {'error': True})
    else:
        return render(request, "booksearch.html", {'error': False})


def booksearch2(request):
    if request.method == 'POST':
        form = BookQueryForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']

            if 'searched' in request.session and request.session['searched'] == name:
                return HttpResponse('Query already made!!!')
            request.session['searched'] = name
            books = Book.objects.filter(title__icontains=name)
            return render(request, 'booklist.html', {'form': form, 'books': books})
    else:
        form = BookQueryForm()
    return render(request, 'form.html', {'form': form})


def author_search(request):
    if request.method == 'POST':
        form = BookQueryAuthorForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            books = Book.objects.filter(authors__in=Author.objects.filter(name__icontains=name))
            return render(request, 'authorlist.html', {'form': form, 'books': books})
    else:
        form = BookQueryAuthorForm()
    return render(request, 'form.html', {'form': form})


def author_publisher_search(request):
    if request.method == 'POST':
        form = BookSearchAuthorPublisherForm(request.POST)
        if form.is_valid():
            authorName = form.cleaned_data['authorName']
            publisherName = form.cleaned_data['publisherName']
            books = Book.objects.filter(authors__name__icontains=authorName, publisher__name__icontains=publisherName)
            return render(request, 'author_publisher_list.html', {'form': form, 'books': books})
    else:
        form = BookSearchAuthorPublisherForm()
    return render(request, 'form.html', {'form': form})


def insert_author(request):
    if not request.user.is_authenticated or request.user.username != 'botto':
        #request.user.is_admin para ver se é admin e n meter o username hardcoded
        return redirect('/login')
    if request.method == 'POST':
        form = InsertAuthor(request.POST)
        if form.is_valid():
            new_author = Author.objects.create(name=form.cleaned_data['name'], email=form.cleaned_data['email'])
            return render(request, 'insert_author.html', {'form': form, 'new_author': new_author, 'success': True})
    else:
        form = InsertAuthor()
    return render(request, 'insert_author.html', {'form': form, 'success': False})


def insert_publisher(request):
    if request.method == 'POST':
        form = InsertPublisher(request.POST)
        if form.is_valid():
            publisher = Publisher.objects.create(name=form.cleaned_data['name'], city=form.cleaned_data['city'],
                                                 country=form.cleaned_data['country'], website=form.cleaned_data[
                    'website'])
            return render(request, 'insert_publisher.html', {'form': form, 'publisher': publisher})
    else:
        form = InsertPublisher()
    return render(request, 'insert_publisher.html', {'form': form})


def insert_book(request):
    if request.method == 'POST':
        form = InsertBook(request.POST)
        if form.is_valid():
            book = Book.objects.create(title=form.cleaned_data['title'], date=form.cleaned_data['date'],
                                       publisher=form.cleaned_data['publisher'])
            book.save()
            book.authors.set(form.cleaned_data['authors'])
            book.save()

            return render(request, 'insert_book.html', {'form': form, 'book': book})
    else:
        form = InsertBook()
    return render(request, 'insert_book.html', {'form': form})


def edit_author(request):
    if request.method == 'POST':
        form = EditAuthor(request.POST)
        if form.is_valid():
            author = form.cleaned_data['author_to_change']
            Author.objects.filter(name=author.name).update(name=form.cleaned_data['new_name'],
                                                           email=form.cleaned_data['new_email'])

            return render(request, 'edit_author.html', {'form': form}, 'autho')
    else:
        form = EditAuthor()
    return render(request, 'edit_author.html', {'form': form})
