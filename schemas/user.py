from pydantic import BaseModel, EmailStr, Field
from .role import RoleResponse

class UserCreate(BaseModel):
    username: str = Field(min_length=3, max_length=35);
    email: EmailStr
    password: str = Field(min_length=5, max_length=50);

class UserResponse(BaseModel):
    id: int
    username: str
    email: str
    roles: list[RoleResponse]

    class Config:
        orm_mode = True
        from_attributes = True

class LoginRequest(BaseModel):
    email: EmailStr
    password: str = Field(min_length=5, max_length=50);

    class Config:
        orm_mode = True;
