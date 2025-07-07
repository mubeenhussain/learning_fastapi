from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from models.product import Product
from schemas.product import ProductCreate, ProductOut
from database import get_db
from core.auth_middleware import auth_middleware
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/login")


router = APIRouter()

@router.post("/auth/product", response_model=ProductOut, status_code=status.HTTP_201_CREATED)
def create_product(
    product: ProductCreate, 
    db: Session = Depends(get_db),
    token: str = Depends(oauth2_scheme)  # <-- This adds the Bearer token field in Swagger

    # auth: str =Depends(auth_middleware)  # <-- Protected
):
    db_product = Product(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

@router.get("/product", response_model=List[ProductOut])
def get_products(db: Session = Depends(get_db)):
    return db.query(Product).all()

@router.get("/product/{product_id}", response_model=ProductOut)
def get_product(product_id: int, db: Session = Depends(get_db)):
    product = db.query(Product).filter(Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@router.put("/auth/product/{product_id}", response_model=ProductOut)
def update_product(product_id: int, product: ProductCreate, db: Session = Depends(get_db),
                       token: str = Depends(oauth2_scheme)  # <-- This adds the Bearer token field in Swagger
):
    db_product = db.query(Product).filter(Product.id == product_id).first()
    if not db_product:
        raise HTTPException(status_code=404, detail="Product not found")
    for key, value in product.dict().items():
        setattr(db_product, key, value)
    db.commit()
    db.refresh(db_product)
    return db_product

@router.delete("/auth/product/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_product(
    product_id: int, 
    db: Session = Depends(get_db),
    token: str = Depends(oauth2_scheme)  # <-- This adds the Bearer token field in Swagger
):
    db_product = db.query(Product).filter(Product.id == product_id).first()
    if not db_product:
        raise HTTPException(status_code=404, detail="Product not found")
    db.delete(db_product)
    db.commit()
    return None