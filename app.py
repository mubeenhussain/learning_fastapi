from fastapi import Depends, FastAPI, Path, HTTPException, status
from typing import Optional
from pydantic import BaseModel
from database import get_db
from schemas.user import UserSchema  # Import the User class
from models.user import UserModal
from schemas.user import LoginSchema
from sqlalchemy.orm import Session  # Import Session for type hinting
from database import Base,engine
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordRequestForm
from jose import jwt
from config import create_access_token

Base.metadata.create_all(bind=engine)

app = FastAPI()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

@app.post('/user', response_model=UserSchema)
def create_user(request: UserSchema, db: Session = Depends(get_db)):
    # Check if email already exists
    user = db.query(UserModal).filter(UserModal.email == request.email).first()
    if user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
        )
    # Hash the password before storing
    hashed_password = hash_password(request.password)
    new_user = UserModal(
        name=request.name,
        email=request.email,
        password=hashed_password
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@app.post('/login')
def login(form_data: LoginSchema = Depends(), db: Session = Depends(get_db)):
    user = db.query(UserModal).filter(UserModal.email == form_data.email).first()
    if not user or not pwd_context.verify(form_data.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password"
        )
    access_token = create_access_token(data={"sub": user.id})

    return {"access_token": access_token, "user":user}