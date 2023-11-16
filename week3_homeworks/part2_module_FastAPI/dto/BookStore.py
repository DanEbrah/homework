from .BookItem import BookItem
from pydantic import BaseModel


class BookStore(BaseModel):
    name: str
    book_shelve: list[BookItem]
