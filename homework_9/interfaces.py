from abc import ABC, abstractmethod
from sqlalchemy.orm import Session

from .entities import (
    BookSchema,
    BookCreateSchema,
    BookUpdateSchema
)
from .models import Book


class LibraryService(ABC):
    @abstractmethod
    def add_book(self, book_data: BookCreateSchema) -> Book | str: ...

    @abstractmethod
    def update_book(self, upd_data: BookUpdateSchema) -> Book: ...


class BookRepository(ABC):
    @abstractmethod
    def add_book(self, db: Session, book_data: BookCreateSchema) -> dict: ...

    @abstractmethod
    def get_book_by_id(self, db: Session, book_id: int) -> Book: ...
