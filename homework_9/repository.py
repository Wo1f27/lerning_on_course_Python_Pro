from sqlalchemy.orm import Session

from .entities import BookCreateSchema
from .interfaces import BookRepository
from .models import Book, BorrowedBook, Reader


class BookRepositoryImpl(BookRepository):
    def add_book(self, db: Session, book_data: BookCreateSchema, quantity: int = 0) -> str:
        existing_book = db.query(Book).filter_by(title=book_data.title, author=book_data.author).first()
        if existing_book:
            return f'Книга с названием {book_data.title} от автора {book_data.author} уже еть в библиотеке'
        db.add(book_data)
        db.commit()
        return f'Книга успешно добавлена'
