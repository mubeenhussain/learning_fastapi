from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database import get_db
from models.cart import Cart, CartItem
from models.product import ProductModal
from typing import List
from pydantic import BaseModel
from schemas.cart import *

router = APIRouter()

# Helper to get or create a cart for a user
def get_or_create_cart(db: Session, user_id: int):
    cart = db.query(Cart).filter(Cart.user_id == user_id).first()
    if not cart:
        cart = Cart(user_id=user_id)
        db.add(cart)
        db.commit()
        db.refresh(cart)
    return cart

@router.get("/", response_model=CartOut)
def get_cart(user_id: int, db: Session = Depends(get_db)):
    cart = db.query(Cart).filter(Cart.user_id == user_id).first()
    if not cart:
        raise HTTPException(status_code=404, detail="Cart not found")
    return cart

@router.post("/add", response_model=CartOut)
def add_to_cart(item: CartItemCreate, user_id: int, db: Session = Depends(get_db)):
    cart = get_or_create_cart(db, user_id)
    cart_item = db.query(CartItem).filter(CartItem.cart_id == cart.id, CartItem.product_id == item.product_id).first()
    if cart_item:
        cart_item.quantity = cart_item.quantity + item.quantity
    else:
        cart_item = CartItem(cart_id=cart.id, product_id=item.product_id, quantity=item.quantity)
        db.add(cart_item)
    db.commit()
    db.refresh(cart)
    return cart

@router.put("/update/{cart_item_id}", response_model=CartOut)
def update_cart_item(cart_item_id: int, quantity: int, user_id: int, db: Session = Depends(get_db)):
    cart_item = db.query(CartItem).filter(CartItem.id == cart_item_id).first()
    if not cart_item:
        raise HTTPException(status_code=404, detail="Cart item not found")
    cart_item.quantity = quantity
    db.commit()
    cart = db.query(Cart).filter(Cart.id == cart_item.cart_id).first()
    return cart

@router.delete("/remove/{cart_item_id}", status_code=status.HTTP_204_NO_CONTENT)
def remove_cart_item(cart_item_id: int, user_id: int, db: Session = Depends(get_db)):
    cart_item = db.query(CartItem).filter(CartItem.id == cart_item_id).first()
    if not cart_item:
        raise HTTPException(status_code=404, detail="Cart item not found")
    db.delete(cart_item)
    db.commit()
    return
