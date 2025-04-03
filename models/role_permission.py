from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from core.database import Base

class RolePermission(Base):
    __tablename__ = "role_permissions"

    permission_id = Column(Integer, ForeignKey("permissions.id", ondelete="CASCADE"), primary_key=True)
    role_id = Column(Integer, ForeignKey("roles.id", ondelete="CASCADE"), primary_key=True)

    permission = relationship("Permission", back_populates="roles")
    role = relationship("Role", back_populates="permissions")
