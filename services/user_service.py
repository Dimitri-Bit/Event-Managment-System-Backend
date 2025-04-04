from typing import Annotated
from fastapi.params import Depends
from repository.user_repository import UserRepository
from schemas.user import UserCreate
from model.user_model import User
from util.password_manager import PasswordManager

class UserService:
    def __init__(self, repository: Annotated[UserRepository, Depends(UserRepository)]):
        self.repository = repository
        self.password_manager = PasswordManager()

    async def add_user(self, register_request: UserCreate) -> User | None:
        db_user = self.map_register_request(register_request)
        db_user = await self.repository.create_user(db_user)
        return db_user

    async def get_user_by_id(self, id: int) -> User | None:
        db_user = await self.repository.get_user_by_id(id);
        return db_user;

    def map_register_request(self, register_request: UserCreate) -> User:
        return User(
            email=register_request.email,
            username=register_request.username,
            password=self.password_manager.get_password_hash(register_request.password)
        )
