from typing import List
from fastapi import APIRouter, HTTPException, status, Depends

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

from product.models import Product
from product.schemas import ProductSchema


engine = create_engine("postgresql://postgres:1@localhost/fastapi_project")
SesssionLocal = sessionmaker(bind=engine)

def get_db():
    db = SesssionLocal()
    try:
        yield db
    finally:
        db.close()

router = APIRouter(prefix='/api')

@router.get("/products/", response_model=List[ProductSchema], status_code=status.HTTP_200_OK)
async def get_products(db: Session = Depends(get_db)):
    return db.query(Product).all()

@router.post("/products/", response_model=ProductSchema, status_code=status.HTTP_201_CREATED)
async def create_product(data: ProductSchema, db: Session = Depends(get_db)):
    product = Product(**data.dict())
    print(product)
    db.add(product)
    db.commit()
    db.refresh(product)
    return product

@router.get("/products/{id}/", response_model=ProductSchema, status_code=status.HTTP_200_OK)
async def get_product(id: int, db: Session = Depends(get_db)):
    product = db.query(Product).filter(Product.id==id).first()
    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Мындай продукт жок!")
    return product


    # DELETE request 
    # DELETE /api/products/1 HTTP/1.1
    # product алууу 
    # product delete 

    # PUT request
    # PUT /api/products/1 HTTP/1.1
    # product алууу      
    # product update