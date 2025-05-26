from fastapi import Depends
from services.base_services import BooksService

books_list = [
    {"id": 1, "title": "1984", "author": "George Orwell"},
    {"id": 2, "title": "To Kill a Mockingbird", "author": "Harper Lee"},
    {"id": 3, "title": "Brave New World", "author": "Aldous Huxley"},
]

def get_books_list() -> list[dict]:
    return books_list

def get_books_service(books_list: list[dict] = Depends(get_books_list)) -> BooksService:
    return BooksService(books_list)
