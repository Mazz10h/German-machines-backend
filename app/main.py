from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from typing import List

from app.database import Base, engine, get_db
from app.models import category as category_model
from app.models import product as product_model
from app.models import order as order_model
from app.schemas import category as category_schema
from app.schemas import product as product_schema
from app.schemas import order as order_schema

# Create tables if they don't exist
Base.metadata.create_all(bind=engine)

# Initialize FastAPI
app = FastAPI(title="Car Dealership API")

# -------------------- CORS --------------------
origins = ["http://localhost:3000", "http://127.0.0.1:3000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -------------------- CATEGORY --------------------
@app.get("/categories/", response_model=List[category_schema.Category])
def get_categories(db: Session = Depends(get_db)):
    return db.query(category_model.Category).all()

@app.post("/categories/", response_model=category_schema.Category)
def create_category(cat: category_schema.CategoryCreate, db: Session = Depends(get_db)):
    new_cat = category_model.Category(name=cat.name)
    db.add(new_cat)
    db.commit()
    db.refresh(new_cat)
    return new_cat

# -------------------- PRODUCT --------------------
@app.get("/products/", response_model=List[product_schema.ProductOut])
def get_products(db: Session = Depends(get_db)):
    products = db.query(product_model.Product).all()
    # Include category name in the output
    return [
        product_schema.ProductOut(
            id=p.id,
            name=p.name,
            brand=p.brand,
            price=p.price,
            category_id=p.category_id,
            category_name=p.category.name,
            image_url=p.image_url
        )
        for p in products
    ]

@app.get("/categories/{category_id}/products/", response_model=List[product_schema.ProductOut])
def get_products_by_category(category_id: int, db: Session = Depends(get_db)):
    products = db.query(product_model.Product).filter(product_model.Product.category_id == category_id).all()
    return [
        product_schema.ProductOut(
            id=p.id,
            name=p.name,
            brand=p.brand,
            price=p.price,
            category_id=p.category_id,
            category_name=p.category.name,
            image_url=p.image_url
        )
        for p in products
    ]

@app.post("/products/", response_model=product_schema.ProductOut)
def create_product(prod: product_schema.ProductCreate, db: Session = Depends(get_db)):
    category = db.query(category_model.Category).filter(category_model.Category.id == prod.category_id).first()
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    new_prod = product_model.Product(
        name=prod.name,
        brand=prod.brand,
        price=prod.price,
        category_id=prod.category_id,
        image_url=prod.image_url
    )
    db.add(new_prod)
    db.commit()
    db.refresh(new_prod)
    return product_schema.ProductOut(
        id=new_prod.id,
        name=new_prod.name,
        brand=new_prod.brand,
        price=new_prod.price,
        category_id=new_prod.category_id,
        category_name=category.name,
        image_url=new_prod.image_url
    )

# -------------------- ORDER --------------------
@app.get("/orders/", response_model=List[order_schema.Order])
def get_orders(db: Session = Depends(get_db)):
    return db.query(order_model.Order).all()

@app.post("/orders/", response_model=order_schema.Order)
def create_order(ord: order_schema.OrderCreate, db: Session = Depends(get_db)):
    product = db.query(product_model.Product).filter(product_model.Product.id == ord.product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    new_order = order_model.Order(product_id=ord.product_id, quantity=ord.quantity)
    db.add(new_order)
    db.commit()
    db.refresh(new_order)
    return new_order
