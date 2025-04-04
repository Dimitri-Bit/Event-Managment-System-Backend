from typing import Annotated
from fastapi.params import Depends
from repository.user_repository import UserRepository
from config import settings
from util.jwt_manager import JWTManager
from util.password_manager import PasswordManager
from model.user_model import User
from typing import Union

class AuthService:
    def __init__(self, repository: Annotated[UserRepository, Depends(UserRepository)]):
        self.repository = repository
        self.jwt_manager = JWTManager(
            secret_key=settings.settings.SECRET_KEY,
            algorithm=settings.settings.HASH_ALGORITHM,
            access_token_expire_minutes = settings.settings.ACCESS_TOKEN_EXPIRE_MINUTES
        )
        self.password_manager = PasswordManager()

    async def authenticate_user(self, email: str, password: str) -> Union[User, bool]:
        user = await self.repository.get_user_by_email(email)

        if user is None:
            return False

        assert isinstance(user, User)

        if not self.password_manager.verify_password(password, user.password):
            return False
        return user

    async def test(self):
        print("Key", settings.settings.SECRET_KEY)
        print("Hash Algorithm", settings.settings.HASH_ALGORITHM)
        print("Token Expire", settings.settings.ACCESS_TOKEN_EXPIRE_MINUTES)
