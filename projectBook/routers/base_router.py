from fastapi import APIRouter, Depends, status, Body
from schemas.base_schemas import Book, SearchModel
from database import get_books_service
from services.base_services import BooksService


router = APIRouter(prefix="/v1/books", tags=["Книги"])


@router.get("/uppercase", status_code=status.HTTP_200_OK, 
            summary="Список книг с названием в верхнем регистре", 
            description="Метод переводит название книги в верхний регистр", 
            response_model=list[Book])
async def get_uppercase(service: BooksService = Depends(get_books_service)):

    return await service.get_uppercase()

@router.post("/search", status_code=status.HTTP_202_ACCEPTED, 
            summary="Поиск в списке книг", 
            description="Метод производит поиск по названию книги или автору", 
            response_model=Book)
async def post_search(search: SearchModel = Body(), service: BooksService = Depends(get_books_service)):
    
    return await service.post_search(search)
