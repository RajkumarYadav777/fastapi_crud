# define user model here

from sqlalchemy.orm import Column, String, Integer, DateTime,Boolean, func
from app.db.base_class import Base

class User(Base):
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False)
    email = Column(String(100), unique=True, nullable=False, index=True)
    password = Column(String(255), nullable=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True),onupdate=func.now())