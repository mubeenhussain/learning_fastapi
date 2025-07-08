from pydantic import BaseModel
from typing import Optional

class ProductCreate(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    quantity: int

class ProductOut(ProductCreate):
    id: int

    class Config: 
        orm_mode = True