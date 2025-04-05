from typing import Annotated
from fastapi import APIRouter
from fastapi.params import Depends
from schemas.auth import Token
from fastapi.security import OAuth2PasswordRequestForm

from services.auth_service import AuthService

router = APIRouter(prefix="/auth", tags=["Auths"])

@router.post(path="/login")
async def login(
    service: Annotated[AuthService, Depends(AuthService)],
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
) -> Token:
    email = form_data.username
    password = form_data.password

    return await service.login(email, password)
