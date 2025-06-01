from django.shortcuts import render, redirect, get_object_or_404

from .models import Book
from .forms import BookAdd


def home(request):
    return render(request, 'library_manage/home.html')


def list_books(request):
    books = Book.objects.all()
    return render(request, 'library_manage/list_books.html', {'books': books})


def add_book(request):
    if request.method == 'POST':
        form = BookAdd(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_books')
    else:
        form = BookAdd()
    return render(request, 'library_manage/add_book.html', {'form': form})


def detail_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return render(request, 'library_manage/detail_book.html', {'book': book})


def update_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        form = BookAdd(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('detail_book', book_id=book.id)
    else:
        form = BookAdd(instance=book)
    return render(request, 'library_manage/update_book.html', {'form': form, 'book': book})


def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        book.delete()
        return redirect('list_books')
    return render(request, 'library_manage/delete_book.html', {'book': book})
