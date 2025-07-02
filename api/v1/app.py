from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from controllers import user_controller
from core.database import get_db
from schemas import user as user_schema

api_router = APIRouter(tags=["Auth"], prefix="/auth")

@api_router.post("/register", response_model=user_schema.UserOut)
def register(user: user_schema.UserCreate, db: Session = Depends(get_db)):
    return user_controller.register_user(user, db)

@api_router.post("/login", response_model=user_schema.Token)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    return user_controller.login_user(form_data, db)