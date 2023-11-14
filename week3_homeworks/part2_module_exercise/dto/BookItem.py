from pydantic import BaseModel, field_validator
from .Author import Author

class BookItem(BaseModel):
    name: str
    published_year: int
    author: Author

    @field_validator("published_year") 
    @classmethod
    def check_published_year(cls, published_year: int): 
        assert published_year >= -3000 and published_year <= 2023, "Has to be between -3000 and 2023"
        return published_year


