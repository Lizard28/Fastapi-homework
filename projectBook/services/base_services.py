from schemas.base_schemas import SearchModel
from fastapi import HTTPException

class BooksService:
    def __init__(self, books_list: list[dict]):
        self.books_list = books_list

    async def post_search(self, search: SearchModel):

        find = None

        for book in self.books_list:
            if search.title == book.title or search.author == book.author:
                find = book

        if not find:
            raise HTTPException(status_code=404, detail="Книга не найдена")

        return find


    async def get_uppercase(self):
        temp = self.books_list

        for i in temp:
            i.title = i.title.upper()

        return temp