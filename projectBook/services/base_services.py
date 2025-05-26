from schemas.base_schemas import SearchModel, BookCreate, BookOutputSchemas, UpdateBook
from fastapi import HTTPException, status
from schemas.base_schemas import Book
from pydantic import ValidationError

class BooksService:
    def __init__(self, books_list: list[dict]):
        self.books_list = books_list

    #функция для создания новой записи
    async def create_book(self, book: BookCreate) -> BookOutputSchemas:
        self.books_list.append({
            "id":self.books_list[-1]["id"]+1 if self.books_list else 1,
            **book.dict() 
        })
        try:
            return BookOutputSchemas(message=f"Книга с id = {self.books_list[-1]['id']} добавлена", 
                                     book = Book(**self.books_list[-1]))
        except ValidationError:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="нарушение pydantic схемы")

    #функция для обновления записи
    async def update_book(self, book_id: int, book: UpdateBook) -> BookOutputSchemas:
        for idx, existing_book in enumerate(self.books_list):
            if existing_book["id"] == book_id:
                updated_book = {"id": book_id, **book.dict()}
                self.books_list[idx] = updated_book
                return BookOutputSchemas(message=f"Книга с id = {book_id} обновлена", 
                                     book = Book(**updated_book))
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Книга с id = {book_id} не найдена")

    #функция для удаления записи
    async def delete_book(self, book_id: int):
        for idx, existing_book in enumerate(self.books_list):
            if existing_book["id"] == book_id:
                self.books_list.pop(idx)
                return
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Книга с id = {book_id} не найдена")

    #функция для перевода названия в верхний регистр
    async def get_uppercase(self):
        temp = [Book(**books_dict) for books_dict in self.books_list]
        for i in temp:
            i.title = i.title.upper()
        return temp

    #функция для поиска по названию или автору
    async def post_search(self, search: SearchModel):
        books_objects = [Book(**books_dict) for books_dict in self.books_list]
        find = None
        for book in  books_objects:
            if search.title == book.title or search.author == book.author:
                find = book
        if not find:
            raise HTTPException(status_code=404, detail="Книга не найдена")
        return find
