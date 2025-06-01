from django import forms

from .models import Book


class BookAdd(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'published_year', 'isbn', 'caption']

