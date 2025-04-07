from model.role_model import Role
from .base import Base
from model.role_user import role_user
from sqlalchemy import select

class RoleRepository(Base):

    async def set_user_role(self, user_id: int, role_name: str):
        query = select(Role).where(Role.name == role_name)
        role = await self.db.execute(query)
        role = role.unique().scalar()

        if role is None:
            pass

        assert isinstance(role, Role)
        role_id = role.id

        await self.db.execute(
            role_user.insert().values(
                user_id=user_id,
                role_id=role_id
            )
        )

        await self.db.commit()
