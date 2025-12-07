from pydantic import BaseModel

# For creating new products
class ProductCreate(BaseModel):
    name: str
    brand: str
    price: float
    category_id: int
    image_url: str

# For returning product data to frontend
class ProductOut(BaseModel):
    id: int
    name: str
    brand: str
    price: float
    category_id: int
    category_name: str
    image_url: str

    class Config:
        from_attributes = True  # replaces orm_mode in Pydantic V2
