from sqlalchemy import Table, Column, ForeignKey
from .base import Base

permission_role = Table(
    "permissions_roles",
    Base.metadata,
    Column("permission_id", ForeignKey("permissions.id"), primary_key=True),
    Column("role_id", ForeignKey("roles.id"), primary_key=True)
);
