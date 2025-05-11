from sqlalchemy.orm import Session

from .entities import Book, BookCreate
from .models import Book, Reader, BorrowedBook

from .interfaces import LibraryService


class LibraryActivity(LibraryService):
    def add_book(self, db: Session, book_data: BookCreate, quantity: int = 0):
        pass

    @staticmethod
    def _is_unique(db: Session, book_data: BookCreate):
        return db.query(Book).filter_by(title=book_data.title, author=book_data.title).first() is None
