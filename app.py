from fastapi import Depends, FastAPI, Path
from typing import Optional
from pydantic import BaseModel
from database import get_db
from schemas.user import UserSchema  # Import the User class
from models.user import UserModal
from sqlalchemy.orm import Session  # Import Session for type hinting
from database import Base,engine

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.post('/user')
def create_user(request: UserSchema, db: Session = Depends(get_db)):
    new_user = UserModal(
        name=request.name,
        email=request.email,
        password=request.password
    )    
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user