from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from schemas.order import OrderCreate, OrderOut
from database import get_db
from models.order import OrderModel
from core.security import get_current_user

router = APIRouter()

@router.post("/add", response_model=OrderOut)
def create_order(order: OrderCreate, db: Session = Depends(get_db), user=Depends(get_current_user)):
    db_order = OrderModel(
        user_id=user.id,  # set user_id from authenticated user
        product_id=order.product_id,
        quantity=order.quantity,
        total_price=order.total_price,
        status=order.status or 'pending'
    )
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order

@router.get("/", response_model=list[OrderOut])
def get_orders(db: Session = Depends(get_db)):
    return db.query(OrderModel).all()

@router.get("/{order_id}", response_model=OrderOut)
def get_order(order_id: int, db: Session = Depends(get_db)):
    order = db.query(OrderModel).filter(OrderModel.id == order_id).first()
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return order

@router.put("/{order_id}", response_model=OrderOut)
def update_order(order_id: int, order: OrderCreate, db: Session = Depends(get_db)):
    db_order = db.query(OrderModel).filter(OrderModel.id == order_id).first()
    if not db_order:
        raise HTTPException(status_code=404, detail="Order not found")
    for key, value in order.dict(exclude_unset=True).items():
        setattr(db_order, key, value)
    db.commit()
    db.refresh(db_order)
    return db_order

@router.delete("/{order_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_order(order_id: int, db: Session = Depends(get_db)):
    db_order = db.query(OrderModel).filter(OrderModel.id == order_id).first()
    if not db_order:
        raise HTTPException(status_code=404, detail="Order not found")
    db.delete(db_order)
    db.commit()
    return
