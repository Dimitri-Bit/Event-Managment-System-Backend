from pydantic import BaseModel, EmailStr, Field
from .role import RoleResponse

class UserCreate(BaseModel):
    username: str = Field(min_length=3, max_length=35);
    email: EmailStr
    password: str = Field(min_length=5, max_length=255);

class UserCreateResponse(BaseModel):
    id: int
    username: str
    email: str
    image_url:str | None

    class Config:
        orm_mode = True
        from_attributes = True

class UserResponse(UserCreateResponse):
    roles: list[RoleResponse]

class UserLogin(BaseModel):
    email: EmailStr
    password: str = Field(min_length=5, max_length=255);

    class Config:
        orm_mode = True;

class UserImageUrlUpdate(BaseModel):
    image_url: str
