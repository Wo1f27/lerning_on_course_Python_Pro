from django.urls import path

from .views import list_books, add_book, detail_book, update_book, delete_book


urlpatterns = [
    path('', list_books, name='list_books'),
    path('<int:book_id>/', detail_book, name='detail_book'),
    path('<int:book_id>/update/', update_book, name='update_book'),
    path('<int:book_id>/delete/', delete_book, name='delete_book'),
    path('add/', add_book, name='add_book'),
]