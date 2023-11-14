from dto import BookItem, BookStore, Author
from pydantic import BaseModel, ValidationError, field_validator

def main():
    author1 = Author(name= "John Doe", 
                     author_id="HDEW-1523")

    print("Book:")
    book_item1 = BookItem(name = "To Kill A Mocking Bird", 
                          published_year = 2000, 
                          author = author1) 
                          
    print(book_item1.__dict__)
    print("\n")

    print("Book Store:")
    book_store = BookStore(name = "Whitcoulls", 
                           book_shelve= [book_item1])
    
    print(book_store.__dict__)
    print("\n")

    #author testing
    try:
        unkown_author = Author(name = "Josh Loe",
                               author_id = "HRQ1-G421")
    except ValidationError as ve:
        print(f"Unknown Author: {unkown_author}")
        print(ve)
    else:
        print(author1.__dict__)

if __name__ == "__main__":
    main()