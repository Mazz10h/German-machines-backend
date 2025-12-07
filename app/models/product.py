from sqlalchemy import Column, Integer, Text, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Product(Base):
    __tablename__ = "product"

    id = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False)
    brand = Column(Text, nullable=False)
    price = Column(Float, nullable=False)
    category_id = Column(Integer, ForeignKey("category.id"))
    image_url = Column(Text, nullable=True)

    # Relationships
    category = relationship("Category", back_populates="products")
    orders = relationship("Order", back_populates="product", cascade="all, delete-orphan")
