from pydantic import BaseModel, field_validator
import re #importing regix

class Author(BaseModel):
    name: str
    author_id: str


    @field_validator("name")
    @classmethod
    def check_valid_name(cls, name: str): 
        assert name.istitle(), "Name needs to start with a capital letter"
        return name

    @field_validator("author_id") 
    @classmethod
    def check_auther_id(cls, author_id: str): 
        id_results = re.search(r"[A-Z]{4}-[0-9]{4}", author_id)
        return id_results != None and len(author_id) == 9

