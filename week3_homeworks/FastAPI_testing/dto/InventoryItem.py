from .ItemOrigin import ItemOrigin
from pydantic import BaseModel

class InventoryItem(BaseModel):
    name: str
    quantity: int
    serial_num: str
    origin: ItemOrigin
