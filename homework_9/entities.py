from pydantic import BaseModel, constr, field_validator


class BookCreate(BaseModel):
    title: constr(max_length=100)
    author: constr(max_length=50)
    published_year: int

    @field_validator('published_year', mode='before')
    def check_year(cls, v):
        if v < 0:
            return ValueError('Год должен быть положительным числом')
        return v


class Book(BookCreate):
    id: int
    quantity: int
