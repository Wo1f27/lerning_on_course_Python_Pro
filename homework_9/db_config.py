from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker, Session

DB_URL = 'postgresql+psycopg2://postgres:1234@localhost:5432/test_for_course'

engine = create_engine(DB_URL)
session = sessionmaker(bind=engine)

Base = declarative_base()


class SessionContext:
    def __enter__(self):
        self.db = session()
        return self.db

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.db.close()


def init_db():
    Base.metadata.create_all()


def get_db() -> Session:
    db = session()
    try:
        yield db
    finally:
        db.close()


if __name__ == '__main__':
    init_db()

