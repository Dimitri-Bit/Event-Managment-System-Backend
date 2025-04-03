from sqlalchemy import Table, Column, ForeignKey
from .base import Base

role_user = Table(
    "role_user",
    Base.metadata,
    Column("role_id", ForeignKey("roles.id"), primary_key=True),
    Column("user_id", ForeignKey("users.id"), primary_key=True)
);
