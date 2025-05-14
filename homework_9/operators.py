from sqlalchemy.orm import Session

from .entities import BookSchema, BookCreateSchema, BookUpdateSchema
from .models import Book, Reader, BorrowedBook

from .interfaces import LibraryService
from .repository import BookRepositoryImpl
from .db_config import SessionContext


class LibraryActivity(LibraryService):

    def __init__(self):
        self.session = SessionContext()
        self.book_repo = BookRepositoryImpl()

    def add_book(self, book_data: BookCreateSchema) -> Book | str:
        with self.session as db:
            res = self.book_repo.add_book(db, book_data)
            new_book = res.get('result')
            db.refresh(new_book)
            return new_book

    def update_book(self, upd_data: BookUpdateSchema) -> Book:
        with self.session as db:
            book = self.book_repo.get_book_by_id(db=db, book_id=upd_data.id)
            if book:
                if upd_data.title is not None:
                    book.title = upd_data.title
                if upd_data.author is not None:
                    book.author = upd_data.author
                if upd_data.published_year is not None:
                    book.published_year = upd_data.published_year
                if upd_data.quantity is not None:
                    book.quantity = upd_data.quantity

                db.commit()
                db.refresh(book)
                return book


