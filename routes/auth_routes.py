from typing import Annotated
from fastapi import APIRouter
from fastapi.params import Depends

from services.auth_service import AuthService

router = APIRouter(prefix="/auth", tags=["Auths"])

@router.post(path="/")
async def test(service: Annotated[AuthService, Depends(AuthService)]):
    test = await service.authenticate_user("user@example.com", "string")
    if not test:
        return {"message": "fuck"}
    else:
        return {"message": "yay"}
