from sqlalchemy import Column, Integer, String
from .base import Base
from sqlalchemy.orm import relationship, backref
from .role_user import role_user

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    email = Column(String(50), nullable=False)
    username = Column(String(35), nullable=False)
    password = Column(String(255), nullable=False)
    image_url = Column(String(255), nullable=True)
    roles = relationship(
        "Role",
        secondary=role_user,
        backref=backref("users", lazy="joined"),
        lazy="joined",
        cascade="all, delete",
        passive_deletes=True
    )
    parties = relationship(
        "Party",
        back_populates="user",
        lazy="joined",
        cascade="all, delete-orphan",
        passive_deletes=True
    )
