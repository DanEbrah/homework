from pydantic import BaseModel, field_validator

class ItemOrigin(BaseModel):
    country: str
    production_date: str

    @field_validator("country") # write custom validator
    @classmethod # you only make method definition to class, trying to wrap around class method
    def check_valid_country(cls, country: str):
        assert country == "Ethiopia", "Country name must be Ethiopa"
        return country