from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .base import Base
from .permission_role import permission_role

class Role(Base):
    __tablename__ = 'roles'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String(40), nullable=True)
    permissions = relationship(
        "Permission",
        secondary=permission_role,
        backref="parents"
    )
