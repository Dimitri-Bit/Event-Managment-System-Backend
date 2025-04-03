from typing import Annotated

from fastapi.params import Depends
from repository.user_repository import UserRepository

from schemas.user import UserCreate
from model.user_model import User

class UserService:
    def __init__(self, repository: Annotated[UserRepository, Depends(UserRepository)]):
        self.repository = repository;

    def add_user(self, register_request:UserCreate) -> User:
        db_user = self.map_register_request(register_request);
        return self.repository.create_user(db_user);

    def map_register_request(self, register_request:UserCreate) -> User:
        return User(
            email=register_request.email,
            username=register_request.username,
            password=register_request.password
        );
