from pydantic import BaseModel, constr, field_validator


class BookCreateSchema(BaseModel):
    title: constr(max_length=100)
    author: constr(max_length=50)
    published_year: int
    quantity: int

    @field_validator('published_year', mode='before')
    def check_year(cls, v):
        if v < 0:
            return ValueError('Год должен быть положительным числом')
        return v

    @field_validator('quantity', mode='before')
    def check_year(cls, v):
        if v < 0:
            return ValueError('Количество должно быть положительным числом')
        return v


class BookSchema(BookCreateSchema):
    id: int
    quantity: int
