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
    def check_quantity(cls, v):
        if v < 0:
            raise ValueError('Количество должно быть положительным числом')
        return v


class BookSchema(BookCreateSchema):
    id: int
    quantity: int


class BookUpdateSchema(BaseModel):
    id: int
    title: constr(max_length=100) | None = None
    author: constr(max_length=50) | None = None
    published_year: int | None = None
    quantity: int | None = None

    @field_validator('published_year', mode='before')
    def check_year(cls, v):
        if v is not None and v < 0:
            raise ValueError('Год должен быть положительным числом')
        return v

    @field_validator('quantity', mode='before')
    def check_quantity(cls, v):
        if v < 0:
            raise ValueError('Количество должно быть положительным числом')
        return v
