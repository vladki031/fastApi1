from fastapi import FastAPI
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from app.models import Base
from app.config import settings
from app.routers import product, order, auth

engine = create_engine(settings.DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(product.router, prefix="/api/products", tags=["products"])
app.include_router(order.router, prefix="/api/orders", tags=["orders"])
app.include_router(auth.router, prefix="/api/auth", tags=["auth"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
