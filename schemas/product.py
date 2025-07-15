from pydantic import BaseModel, Field
from typing import Optional

class ProductBase(BaseModel):
    slug: Optional[str] = None
    title: str
    description: Optional[str] = None
    price: float
    sell_price: Optional[float] = None
    discount: Optional[float] = None
    quantity: Optional[int] = 0
    in_stock: Optional[bool] = True

class ProductCreate(ProductBase):
    pass

class ProductOut(ProductBase):
    id: int
    # owner_id: int

    class Config:
        orm_mode = True
