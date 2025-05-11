from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker, Session

DB_URL = 'postgresql+psycopg2://postgres:1234@localhost:5432/test_for_course'

engine = create_engine(DB_URL)
session = sessionmaker(bind=engine)

Base = declarative_base()


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

