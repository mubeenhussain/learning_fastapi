from fastapi import APIRouter, Depends
from schemas.product import ProductCreateSchema
from database import get_db

router = APIRouter()

@router.post("/add")
def add_product(data:ProductCreateSchema):
    return {
        "data": data    
    }