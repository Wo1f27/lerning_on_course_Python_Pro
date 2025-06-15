from sqlalchemy import Column, Integer, Text, DateTime
from .db import Base


class Task(Base):
    __table_name__ = 'tasks'

    id = Column(Integer, primary_key=True)
    name = Column(Text, max_length=500)
    deadline = Column(DateTime)
