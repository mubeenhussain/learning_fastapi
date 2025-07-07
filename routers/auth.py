from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from schemas.user import UserCreate, UserOut, LoginSchema
from models.user import UserModal
from database import get_db
from core.security import hash_password, verify_password, create_access_token
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi import FastAPI, UploadFile


router = APIRouter()

@router.post("/register", response_model=UserOut)
def register(user: UserCreate, db: Session = Depends(get_db)):
    if db.query(UserModal).filter(UserModal.email == user.email).first():
        raise HTTPException(status_code=400, detail="Email already registered")
    new_user = UserModal(
        name=user.name,
        email=user.email,
        password=hash_password(user.password)
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(UserModal).filter(UserModal.email == form_data.username).first()
    if not user or not verify_password(form_data.password, user.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    access_token = create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "user":user}


@router.post("/file")
async def upload_file(file: UploadFile):
    filename = file.filename
    content = await file.read()
    return {
        "filename": filename,
        "content":content
    }