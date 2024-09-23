from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.schemas import OrderCreate, OrderResponse
from app.models import Order, Product, User
from app.routers.auth import get_current_user
from app.main import get_db

router = APIRouter()

@router.post("/", response_model=OrderResponse)
def create_order(order: OrderCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    total_amount = 0
    products_in_order = []

    for item in order.products:
        product = db.query(Product).filter(Product.id == item.product_id).first()
        if product is None:
            raise HTTPException(status_code=404, detail=f"Product {item.product_id} not found")
        if product.quantity_in_stock < item.quantity:
            raise HTTPException(status_code=400, detail=f"Not enough stock for product {product.name}")
        product.quantity_in_stock -= item.quantity
        products_in_order.append(product)
        total_amount += product.price * item.quantity

    new_order = Order(user_id=current_user.id, products=products_in_order, total_amount=total_amount)
    db.add(new_order)
    db.commit()
    db.refresh(new_order)

    return new_order

@router.get("/user", response_model=List[OrderResponse])
def get_user_orders(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return db.query(Order).filter(Order.user_id == current_user.id).all()
