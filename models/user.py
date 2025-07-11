from sqlalchemy import Column, Integer, String, JSON
from database import Base
from sqlalchemy.orm import relationship

class UserModal(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)
    roles = Column(JSON, default=list)
    
    
    # 1 to many relationship built
    tasks = relationship("TaskModel", back_populates="owner")
    
    # 1 to 1 relationship 
    profile = relationship("ProfileModal", back_populates="user", uselist=False)
    
    posts = relationship("Post", backref='author')