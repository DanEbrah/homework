from dto import InventoryItem, ItemOrigin
from typing import Dict, List
from fastapi import FastAPI, HTTPException

app = FastAPI()


my_inventory_items_dict: Dict[str, InventoryItem] = {} #empty dict

@app.put("/items/{serial_num}") #put req
def create_item(item: InventoryItem, serial_num: str) -> None:#first time and serial num to look up
    my_inventory_items_dict[serial_num] = item #use serial num to get the item
    print(my_inventory_items_dict)

@app.get("/items/{serial_num}") 
def get_item(serial_num: str) -> InventoryItem:
    if serial_num in my_inventory_items_dict.keys():
        return my_inventory_items_dict[serial_num]
    else:
        raise HTTPException(status_code=404, detail="Item not found")

@app.delete("/items/{serial_num}")
def delete_item(serial_num: str) -> Dict:
    if serial_num in my_inventory_items_dict.keys():
        my_inventory_items_dict.pop(serial_num)
        print(my_inventory_items_dict)
        return {"msg": "deleted"}
    else:
        raise HTTPException(status_code=404, detail="Item not found")   
    

@app.get("/items/")
def get_items() ->List[InventoryItem]:
    return my_inventory_items_dict.values()
    