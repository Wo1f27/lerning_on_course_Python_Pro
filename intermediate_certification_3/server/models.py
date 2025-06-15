from sqlalchemy import Column, Integer, String, DateTime
from .db import Base


class Task(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True)
    name = Column(String(500))
    deadline = Column(DateTime)
