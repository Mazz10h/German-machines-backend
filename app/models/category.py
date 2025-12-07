from sqlalchemy import Column, Integer, Text
from sqlalchemy.orm import relationship
from app.database import Base

class Category(Base):
    __tablename__ = "category"

    id = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False, unique=True)

    # Relationship to products
    products = relationship("Product", back_populates="category", cascade="all, delete-orphan")
