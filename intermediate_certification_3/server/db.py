from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import declarative_base, sessionmaker


DATABASE_URL = 'sqlite:///tg_bot_database'

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
metadata = MetaData()
Base = declarative_base()
