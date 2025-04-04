from sqlalchemy import Column, Integer, String, Text, Float, DateTime,ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class Party(Base):
    __tablename__ = "parties"

    id = Column(Integer, primary_key=True, index=True)
    name_party = Column(String(255), nullable=False)
    url_image_full = Column(String(500), nullable=False)
    name_organizer = Column(String(255), nullable=False)
    date_start = Column(DateTime, nullable=False)
    date_end = Column(DateTime, nullable=False)
    name_town = Column(String(255), nullable=False)
    name_country = Column(String(255), nullable=False)
    name_type = Column(String(255), nullable=False)
    text_entry_fee = Column(Float, nullable=True)  
    text_more = Column(Text, nullable=True) 
    url_organizer = Column(String(500), nullable=True)  
    url_party = Column(String(500), nullable=True)

    user_id = Column(Integer, ForeignKey("users.id"), nullable=False) 
    user = relationship("User", back_populates="parties")  

    class Config:
        orm_mode = True
