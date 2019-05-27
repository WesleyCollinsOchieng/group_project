from django.shortcuts import render
from .models import Book, Book_itself, Authors
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
def index(request):
    books = Book.objects.filter(user=request.user)
    context ={
        'books': books
    }

    return render(request, 'book_app/index.html', context)
def details(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render(request, 'book_app/details.html', {'book': book})

def categories(request):
    books = Book.objects.filter(user=request.user)
    context = {
        'books': books
    }

    return render(request, 'book_app/categories.html', context)

def authors(request):
    writer = Authors.objects.all()
    context = {
        'writer': writer
    }

    return render(request, 'book_app/authors.html', context)
def best_books(request):
    books = Book.objects.filter(user=request.user)
    context = {
        'books': books
    }

    return render(request, 'book_app/best_books.html', context)

def library(request):
    books = Book.objects.filter(user=request.user)
    context = {
        'books': books
    }

    return render(request, 'book_app/authors.html', context)
def notifications(request):
    books = Book.objects.filter(user=request.user)
    context = {
        'books': books
    }

    return render(request, 'book_app/authors.html', context)

