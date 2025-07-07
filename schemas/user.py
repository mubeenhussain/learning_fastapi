from pydantic import BaseModel, EmailStr
from typing import List
from .enums import RoleEnum

class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str
    roles: List[RoleEnum] = [RoleEnum.USER]

class UserOut(BaseModel):
    id: int
    name: str
    email: str
    # password: str
    # roles: List
    
    class Config:
        orm_mode = True 
        # now i dont need to dict its variable      

class LoginSchema(BaseModel):
    email: str
    password: str