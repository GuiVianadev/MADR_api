from pydantic import BaseModel


class Book(BaseModel):
    year: int
    title: str
    author_id: int


class BookResponse(BaseModel):
    id: int
    year: int
    title: str
    author_id: int
