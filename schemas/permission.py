from pydantic import BaseModel

class PremCreate(BaseModel):
    name: str
    description: str


class PremResponse(BaseModel):
    id: int
    name: str
    description: str

    class Config:
        orm_mode = True
