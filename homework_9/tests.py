import pytest
from .models import Book, BorrowedBook, Reader
from .entities import (
    BookCreateSchema,
    BookUpdateSchema,
    BookSchema
)
from .db_config import SessionContext
from .operators import LibraryActivity


book: Book = Book(
    title='Book-1-Test',
    author='Author-1-Test',
    published_year=2011,
    quantity=1
)


@pytest.fixture(scope='module')
def library_activity() -> LibraryActivity:
    """Фикстура для LibraryActivity"""
    with SessionContext() as db:
        activity = LibraryActivity()
        yield activity


def test_add_book(library_activity):
    book.title += '_1'
    result = library_activity.add_book(book)
    assert isinstance(result, Book)


def test_update_book(library_activity):
    book.title += '_2'
    create_book = library_activity.add_book(book)
    assert isinstance(create_book, Book), create_book
    book_id = create_book.id
    upd_data = BookUpdateSchema(
        id=book_id,
        title='Book_upd_2',
        author='Author_2'
    )

    updated_book = library_activity.update_book(upd_data=upd_data)
    book_id = updated_book.id
    assert updated_book.title == 'Book_upd_2'
    assert updated_book.author == 'Author_2'


