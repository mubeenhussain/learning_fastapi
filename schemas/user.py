from pydantic import BaseModel

class UserSchema(BaseModel):
    name:str
    email:str
    password:str
    

class LoginSchema(BaseModel):
    email: str
    password: str