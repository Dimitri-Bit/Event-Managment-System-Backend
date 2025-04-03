from pydantic import BaseModel
from .permission import PremResponse

class RoleCreate(BaseModel):
    name: str
    description: str


class RoleResponse(BaseModel):
    id: int
    name: str
    description: str
    permissions: list[PremResponse]

    class Config:
        orm_mode = True
