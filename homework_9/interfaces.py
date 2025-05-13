from abc import ABC, abstractmethod
from sqlalchemy.orm import Session

from .entities import BookSchema, BookCreateSchema


class LibraryService(ABC):
    @abstractmethod
    def add_book(self, book_data: BookCreateSchema) -> str: ...


class BookRepository(ABC):
    @abstractmethod
    def add_book(self, db: Session, book_data: BookCreateSchema, quantity: int = 0) -> str: ...
