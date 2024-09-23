from pydantic import BaseModel
from typing import List
from decimal import Decimal


class ProductCreate(BaseModel):
    name: str
    description: str
    price: Decimal
    quantity_in_stock: int


class ProductResponse(BaseModel):
    id: int
    name: str
    description: str
    price: Decimal
    quantity_in_stock: int

    class Config:
        orm_mode = True


class OrderProduct(BaseModel):
    product_id: int
    quantity: int


class OrderCreate(BaseModel):
    products: List[OrderProduct]


class OrderResponse(BaseModel):
    id: int
    total_amount: Decimal
    products: List[ProductResponse]

    class Config:
        orm_mode = True
