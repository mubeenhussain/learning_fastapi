from sqlalchemy import Column, Integer, String, ForeignKey, Float
from database import Base
from sqlalchemy.orm import relationship


class OrderModel(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)  # If you have a users table
    product_id = Column(Integer, ForeignKey('products.id'), nullable=False)
    quantity = Column(Integer, default=1)
    total_price = Column(Float, nullable=False)
    status = Column(String, default='pending')

    # Relationships (optional)
    # product = relationship("ProductModal")
    # user = relationship("UserModel")