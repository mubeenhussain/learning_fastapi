from sqlalchemy import Column, Integer, String, JSON, ForeignKey, Float, Boolean
from database import Base
from sqlalchemy.orm import relationship

class ProductModal(Base):
    __tablename__ = 'products'
    
    id = Column(Integer, primary_key=True, index=True)
    slug = Column(String, unique=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String)
    price = Column(Integer)
    sell_price = Column(Integer)
    discount = Column(Integer)
    quantity = Column(Integer, default=0)
    in_stock = Column(Boolean, default=True)