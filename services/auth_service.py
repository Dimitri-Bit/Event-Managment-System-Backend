from typing import Annotated
from fastapi import Depends, HTTPException, status
from jwt import InvalidTokenError
from repository.user_repository import UserRepository
from config import settings
from util.jwt_manager import JWTManager
from util.password_manager import PasswordManager
from model.user_model import User
from typing import Union
from schemas.auth import Token

class AuthService:
    def __init__(self, repository: Annotated[UserRepository, Depends(UserRepository)]):
        self.repository = repository
        self.jwt_manager = JWTManager(
            secret_key=settings.settings.SECRET_KEY,
            algorithm=settings.settings.HASH_ALGORITHM,
            access_token_expire_minutes = settings.settings.ACCESS_TOKEN_EXPIRE_MINUTES
        )
        self.password_manager = PasswordManager()

    async def get_current_user(self, token:str) -> User:
        credentials_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
        try:
            payload = self.jwt_manager.decode_token(token)
            assert isinstance(payload, dict)
            email = payload.get("sub")
            if email is None:
                raise credentials_exception
        except InvalidTokenError:
            raise credentials_exception

        user = await self.repository.get_user_by_email(email)
        if user is None:
            raise credentials_exception
        return user

    async def authenticate_user(self, email: str, password: str) -> Union[User, bool]:
        user = await self.repository.get_user_by_email(email)

        if user is None:
            return False

        assert isinstance(user, User)

        if not self.password_manager.verify_password(password, user.password):
            return False
        return user

    async def login(self, email: str, password: str) -> Token:
        user = await self.authenticate_user(email, password)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect username or password",
                headers={"WWW-Authenticate": "Bearer"},
            )

        assert isinstance(user, User)
        access_token = self.jwt_manager.create_access_token(data={"sub": user.email})
        return Token(access_token=access_token, token_type="bearer")

    async def test(self):
        print("Key", settings.settings.SECRET_KEY)
        print("Hash Algorithm", settings.settings.HASH_ALGORITHM)
        print("Token Expire", settings.settings.ACCESS_TOKEN_EXPIRE_MINUTES)
