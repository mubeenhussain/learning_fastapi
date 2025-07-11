from pydantic import BaseModel, Field
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
        

class ProductCreateSchema(BaseModel):
    name: str = Field(...,min_length=1, max_length=100)
    price: float = Field(..., gt=0,  )
    discount: float = Field(0.0, le=10.0)
    in_stock : bool = Field(True) 
    
        
        
class UserDetail(BaseModel):
    name: str
    age: int
    
class Address(BaseModel):
    street: str
    city: str