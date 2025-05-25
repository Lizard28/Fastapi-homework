from pydantic import BaseModel

class Book(BaseModel):
    id: int # уникальный идентификатор книги.
    title: str # наименование книги.
    author: str # автор книги.

class SearchModel(BaseModel):
    title: str = None # наименование книги.
    author: str = None # автор книги.