from pydantic import BaseModel, Field
from typing import Optional, List

# Pydantic schemas for cart operations
class CartItemCreate(BaseModel):
    product_id: int
    quantity: int = 1

class CartItemOut(BaseModel):
    id: int
    product_id: int
    quantity: int
    class Config:
        orm_mode = True

class CartOut(BaseModel):
    id: int
    user_id: int
    items: List[CartItemOut]
    class Config:
        orm_mode = True