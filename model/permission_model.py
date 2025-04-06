from sqlalchemy import Column, Integer, String
from .base import Base

class Permission(Base):
    __tablename__ = 'permissions'
    id = Column(Integer, primary_key=True)
    name = Column(String(35), nullable=False)
    description = Column(String(255), nullable=True)
