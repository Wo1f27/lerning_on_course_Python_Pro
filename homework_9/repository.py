from typing import Optional

from sqlalchemy.orm import Session

from .entities import BookCreateSchema
from .interfaces import BookRepository
from .models import Book, BorrowedBook, Reader


class BookRepositoryImpl(BookRepository):
    def add_book(self, db: Session, book_data: BookCreateSchema) -> dict:
        existing_book = db.query(Book).filter_by(title=book_data.title, author=book_data.author).first()
        if existing_book:
            return {
                'success': False,
                'result': f'Книга с названием {book_data.title} от автора {book_data.author} уже еть в библиотеке'
            }
        new_book = Book(
            title=book_data.title,
            author=book_data.author,
            published_year=book_data.published_year,
            quantity=book_data.quantity
        )
        db.add(new_book)
        db.commit()
        return {'success': True, 'result': new_book}

    def get_book_by_id(self, db: Session, book_id: int) -> Optional[Book]:
        book = db.query(Book).filter_by(id=book_id).first()

        return book


