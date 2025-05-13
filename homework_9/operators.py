from sqlalchemy.orm import Session

from .entities import BookSchema, BookCreateSchema
from .models import Book, Reader, BorrowedBook

from .interfaces import LibraryService
from .repository import BookRepositoryImpl
from .db_config import SessionContext


class LibraryActivity(LibraryService):

    def __init__(self):
        self.session = SessionContext()
        self.book_repo = BookRepositoryImpl()

    def add_book(self, book_data: BookCreateSchema) -> str:
        with self.session as db:
            res = self.book_repo.add_book(db, book_data)
            return res



