from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import select
from sqlalchemy.orm import joinedload

from model.role_model import Role
from .base import Base
from model.user_model import User

class UserRepository(Base):
    async def create_user(self, user: User) -> User:
        try:
            self.db.add(user)
            await self.db.commit()
            await self.db.refresh(user)
            return user
        except SQLAlchemyError as e:
            await self.db.rollback()
            print(f"Database error occurred: {e}")
            raise e

    async def get_users(self):
        try:
            result = await self.db.execute(select(User))
            return result.scalars().all()
        except Exception as e:
            print(f"Error fetching users: {e}")
            raise e

    async def get_user_by_id(self, id:int) -> User | None:
        try:
            result = await self.db.execute(select(User).options(joinedload(User.roles).joinedload(Role.permissions)).filter(User.id==id))
            return result.scalar()
        except Exception as e:
            print(f"Error fetching users: {e}")
            raise e

    async def delete_users(self, user_id: int):
        try:
            result = await self.db.execute(select(User).filter(User.id == user_id))
            user = result.scalars().first()

            if not user:
                return None

            await self.db.delete(user)
            await self.db.commit()
            return user
        except SQLAlchemyError as e:
            print(f"Database error occurred: {e}")
            await self.db.rollback()
            raise e
