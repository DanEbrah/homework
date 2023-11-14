from dto import InventoryItem, ItemOrigin
from pydantic import BaseModel, field_validator

def main():
    itemOrigin = ItemOrigin(country= "Ethiopia", production_date = "02/12/2023")
    
    my_item1 = InventoryItem(name ="Printer",
                             quantity = 10,
                             serial_num = "HDOUSDNM",
                             origin = itemOrigin)
    
    my_serialized_object1 = my_item1.__dict__
    print(my_serialized_object1)
    my_item2 = InventoryItem(**my_serialized_object1)
    print(my_item2.__dict__)


if __name__ == "__main__":
    main()


 