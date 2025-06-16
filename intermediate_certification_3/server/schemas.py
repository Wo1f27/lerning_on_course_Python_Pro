from pydantic import BaseModel, ConfigDict
from datetime import datetime


class TaskSchema(BaseModel):
    id: int
    name: str
    deadline: datetime

    model_config = ConfigDict(
        json_encoders={
            datetime: lambda d: d.strftime('%d.%m.%Y')
        }
    )


class TaskCreate(BaseModel):
    name: str
    deadline: datetime


