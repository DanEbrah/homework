from fastapi import FastAPI, HTTPException
from typing import Dict, List #You can import, list, dict, final

from dto import BookItem


app = FastAPI()

my_book_item_dict: Dict[str, BookItem] = {} #book item dict
#my_book_item_dict2: Dict[str, BookItem]
#my_book_item_dict3: Dict[str, BookItem]

@app.put("/Book_items/{name}") #put/create
def create_book_item(book_item: BookItem, name: str) -> None: #hint
    my_book_item_dict[name] = book_item
    print(my_book_item_dict)

@app.get("/Book_items/{name}") 
def get_book_item(name: str) -> BookItem: #hint
    if name in my_book_item_dict.keys(): #checking for the key name given
        return my_book_item_dict[name] #return it if found
    else:
        raise HTTPException(status_code=404, detail="Book Item not found") #error 404 displays if the book has not been found

@app.delete("/Book_items/{name}") #deleting a book item 
def delete_item(name: str) -> Dict: #hint
    if name in my_book_item_dict.keys(): #checking for name key
       my_book_item_dict.pop(name) #if name key found, pop it.
       print(my_book_item_dict)
       return {"msg": "Book item has been deleted"}
    else:
        raise HTTPException(status_code=404, detail="Book Item not found for deletion")   
    
@app.get("/Book_items/") #get all book items
def get_book_item() ->List[BookItem]:
    return my_book_item_dict.values()