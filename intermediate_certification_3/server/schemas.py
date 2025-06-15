from pydantic import BaseModel
from datetime import datetime


class TaskCreate(BaseModel):
    name: str
    deadline: datetime


