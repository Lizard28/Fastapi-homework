from pydantic import BaseModel

class Book(BaseModel):
    id: int # уникальный идентификатор книги.
    title: str # наименование книги.
    author: str # автор книги.

class SearchModel(BaseModel):
    title: str = None # наименование книги.
    author: str = None # автор книги.

class BookCreate(BaseModel):
    title: str
    author: str

class BookOutputSchemas(BaseModel):
    message: str
    book:Book

class UpdateBook(BookCreate):
    pass
