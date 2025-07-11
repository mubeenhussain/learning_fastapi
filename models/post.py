from database import Base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey

class Post(Base):
    __tablename__ = 'post'
    
    id = Column(Integer,primary_key=True,index=True)
    title = Column(String)
    description = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))
    