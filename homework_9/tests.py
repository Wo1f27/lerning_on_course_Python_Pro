import pytest
from .models import Book, BorrowedBook, Reader
from .entities import BookCreateSchema, BookSchema
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
    result = library_activity.add_book(book)
    assert result == 'Книга успешно добавлена'


