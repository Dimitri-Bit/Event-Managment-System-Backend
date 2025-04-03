from pydantic import BaseModel

class RoleCreate(BaseModel):
    name: str
    description: str


class RoleResponse(BaseModel):
    id: int
    name: str
    description: str

    class Config:
        orm_mode = True
