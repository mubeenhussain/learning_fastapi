from pydantic import BaseModel
from typing import Optional

class OrderCreate(BaseModel):
    user_id: int
    product_id: int
    quantity: int = 1
    total_price: float
    status: Optional[str] = 'pending'

class OrderOut(BaseModel):
    id: int
    user_id: int
    product_id: int
    quantity: int
    total_price: float
    status: str

    class Config:
        orm_mode = True 