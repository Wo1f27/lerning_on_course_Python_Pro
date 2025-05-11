from abc import ABC, abstractmethod
from sqlalchemy.orm import Session

from .entities import Book, BookCreate


class LibraryService(ABC):
    @abstractmethod
    def add_book(self, db: Session, book_data: BookCreate, quantity: int = 0):
        pass
