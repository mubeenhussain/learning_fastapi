from database import Base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship

class ProfileModel(Base):
    __tablename__ = "profile"
    
    id = Column(Integer, primary_key=True, index=True)
    bio = Column(String)
    profile_picture = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'), unique=True)
    
    user = relationship("UserModal",back_populates="profile")