from fastapi import APIRouter, Depends, status, Body
from schemas.base_schemas import Book, SearchModel, BookCreate, UpdateBook, BookOutputSchemas
from database import get_books_service, books_list
from services.base_services import BooksService

router = APIRouter(prefix="/v1/books", tags=["Книги"])

#получения списка книг
@router.get("", status_code=status.HTTP_200_OK,
            summary="Список книг", 
            description="Метод возвращает список книг", 
            response_model=list[Book])

async def get_books():
    return books_list

#создание новой записи
@router.post("/books-create", status_code=status.HTTP_201_CREATED,
            summary="Добавление книги", 
            description="Метод добавляет новую книгу в список",
            response_model=BookOutputSchemas)

async def create_book(book:BookCreate = Body(), service: BooksService = Depends(get_books_service)):
    return await service.create_book(book)
    
#обновление записи
@router.put("/{book_id}", status_code=status.HTTP_200_OK, 
            summary="Обновление записи", 
            description="Метод обновляет запись книги по идентификатору",
            response_model=BookOutputSchemas)

async def update_book(book_id: int, book: UpdateBook, service: BooksService = Depends(get_books_service)):
    return await service.update_book(book_id, book)

#удаление записи
@router.delete("/{book_id}",status_code=status.HTTP_204_NO_CONTENT, 
            summary="Удаление книги", 
            description="Метод удаляет книги по идентификатору")

async def delete_book(book_id: int, service: BooksService = Depends(get_books_service)):
    return await service.delete_book(book_id)

#перевод названия в верхний регистр
@router.get("/uppercase", status_code=status.HTTP_200_OK, 
            summary="Список книг с названием в верхнем регистре", 
            description="Метод переводит название книги в верхний регистр", 
            response_model=list[Book])

async def get_uppercase(service: BooksService = Depends(get_books_service)):
    return await service.get_uppercase()

#поиск по названию или автору
@router.post("/search", status_code=status.HTTP_200_OK, 
            summary="Поиск в списке книг", 
            description="Метод производит поиск по названию книги или автору", 
            response_model=Book)

async def post_search(search: SearchModel = Body(), service: BooksService = Depends(get_books_service)):
    return await service.post_search(search)

