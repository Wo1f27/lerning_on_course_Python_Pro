from datetime import datetime
from sqlalchemy import (
    CheckConstraint,
    DateTime,
    ForeignKey,
    Integer,
    String,

)
from sqlalchemy.orm import mapped_column, Mapped
from homework_9.db_config import Base


class Book(Base):
    __tablename__ = 'books'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(100), nullable=False)
    author: Mapped[str] = mapped_column(String(50), nullable=False)
    published_year: Mapped[int] = mapped_column(Integer)
    quantity: Mapped[int] = mapped_column(Integer, nullable=False)

    __table_args__ = (
        CheckConstraint('quantity >= 0', name='quantity_is_not_negative'),
    )


class Reader(Base):
    __tablename__ = 'readers'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    email: Mapped[str] = mapped_column(String(100), unique=True)


class BorrowedBook(Base):
    __tablename__ = 'borrowed_books'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    book_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey('books.id', ondelete='NO ACTION', onupdate='CASCADE')
    )
    reader_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey('readers.id', ondelete='NO ACTION', onupdate='CASCADE')
    )
    borrow_date: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    return_date: Mapped[datetime] = mapped_column(DateTime)


if __name__ == '__main__':
    print('Tables:')
    for table in Base.metadata.tables:
        print(table)
