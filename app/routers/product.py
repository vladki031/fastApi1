from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.schemas import ProductCreate, ProductResponse
from app.models import Product
from app.main import get_db

router = APIRouter()

@router.get("/", response_model=List[ProductResponse])
def list_products(db: Session = Depends(get_db), in_stock: bool = True):
    products = db.query(Product).filter(Product.quantity_in_stock > 0 if in_stock else True).all()
    return [product.as_dict() for product in products]

@router.get("/{id}", response_model=ProductResponse)
def get_product(id: int, db: Session = Depends(get_db)):
    product = db.query(Product).filter(Product.id == id).first()
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return product.as_dict()
