from typing import Annotated, List, Sequence
from fastapi import HTTPException, status
from fastapi.params import Depends
from model.role_model import Role
from repository.role_repository import RoleRepository
from repository.user_repository import UserRepository
from schemas.user import UserCreate, UserResponse
from model.user_model import User
from util.password_manager import PasswordManager

class UserService:
    def __init__(
        self,
        repository: Annotated[UserRepository, Depends(UserRepository)],
        role_repository: Annotated[RoleRepository, Depends(RoleRepository)]
    ):
        self.repository = repository
        self.role_repository = role_repository
        self.password_manager = PasswordManager()

    async def add_user(self, register_request: UserCreate) -> User | None:
        db_user = self.map_register_request(register_request)
        db_user = await self.repository.create_user(db_user)
        user_id = db_user.id
        assert isinstance(user_id, int)
        await self.role_repository.set_user_role(user_id, "user")
        updated_user = await self.repository.get_user_by_id(user_id)
        return updated_user

    async def get_user_by_id(self, user_id: int, user: User):
        if not self.check_admin_role(user.roles):
            raise HTTPException(status.HTTP_401_UNAUTHORIZED, "You can't do that big boy")

        return await self.repository.get_user_by_id(user_id);

    async def get_all_users(self, user: User):
        if not self.check_admin_role(user.roles):
            raise HTTPException(status.HTTP_401_UNAUTHORIZED, "You can't do that big boy")

        return await self.repository.get_users()

    async def update_user_image_url(self, user_email: str, image_url: str):
        try:
            user = await self.repository.update_user_image_url(user_email, image_url)
            return user
        except Exception as e:
            raise e

    def map_register_request(self, register_request: UserCreate) -> User:
        return User(
            email=register_request.email,
            username=register_request.username,
            password=self.password_manager.get_password_hash(register_request.password)
        )

    def check_admin_role(self, roles:Sequence[Role]):
        for role in roles:
            role_name = role.name
            assert isinstance(role, Role)
            if role_name == "admin":
                return True
        return False
