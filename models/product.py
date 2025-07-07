from sqlalchemy import Column, Integer, String, Float
from database import Base

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    price = Column(Float, nullable=False)
    quantity = Column(Integer, nullable=False)
    
    def dic(self):
        return {
            "id":self.id,
            "name":self.name,
            "description": self.description,
            "price": self.price,
            "quantity": self.quantity
        }