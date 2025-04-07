from typing import Annotated
from fastapi import APIRouter, HTTPException, status
from fastapi.params import Depends
from schemas.user import UserCreate
from services.user_service import UserService
from schemas.user import UserResponse, UserImageUrlUpdate
from fastapi.security import OAuth2PasswordBearer
from services.auth_service import AuthService
from schemas.user import UserListResponse

router = APIRouter(prefix="/users", tags=["Users"])

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

@router.post(path="/", summary="Register a new user in the database", response_model=UserResponse)
async def register_user(user: UserCreate, service: Annotated[UserService, Depends(UserService)]):
    """
    This endpoint allows you to register a new user by providing necessary details such as the user's name,
    email, password, and any other required information in the form of a `UserCreate` schema. Upon successful
    creation, the newly registered user's details will be returned in the response.
    """
    user_response = await service.add_user(user)
    return user_response;

@router.get(path="/me", response_model=UserResponse)
async def get_current_user(
    auth_service: Annotated[AuthService, Depends(AuthService)],
    token: Annotated[str, Depends(oauth2_scheme)]
):
    """
    Get info about current authenticated user
    """
    user = await auth_service.get_current_user(token)
    return user;

@router.get(path="", response_model=UserListResponse)
async def get_all_users(
    service: Annotated[UserService, Depends(UserService)],
    auth_service: Annotated[AuthService, Depends(AuthService)],
    token: Annotated[str, Depends(oauth2_scheme)]
):
    try:
        user = await auth_service.get_current_user(token)
        users = await service.get_all_users(user)  # Assuming this returns a list of User objects
        return {"users": users}  # Wrap the list in a dictionary with key 'users'
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(e))

@router.put(path="/image", response_model=UserResponse)
async def update_user_image(
    user_update: UserImageUrlUpdate,
    service: Annotated[UserService, Depends(UserService)],
    auth_service: Annotated[AuthService, Depends(AuthService)],
    token: Annotated[str, Depends(oauth2_scheme)]
):
    try:
        user = await auth_service.get_current_user(token);
        user_email = user.email
        assert isinstance(user_email, str)
        updated_user = await service.update_user_image_url(user_email, user_update.image_url)
        return updated_user
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))

# @router.get(path="/",summary="Retrieve a list of all users from the database", response_model=list[UserResponse])
# def get_all_users(db: Session = Depends(get_db)):
#     """
#     This endpoint fetches and returns a list of all users stored in the system. Each user is represented by a
#     `UserResponse` schema, containing user details such as their name, email, role, and more. This is useful
#     for administrators or users who need to view all registered users.
#     """
#     users = get_users(db)
#     return users

# @router.put(path="/{user_id}",summary="Update an existing user's details by ID", response_model=UserResponse)
# def update_users(user_id: int, user: UserCreate, db: Session = Depends(get_db)):
#     """
#     This endpoint allows you to update the details of an existing user identified by their unique `user_id`.
#     The updated data should be provided in the form of a `UserCreate` schema. If the user does not exist or
#     if there is an error during the update, a 404 HTTP exception will be raised. Upon success, the updated user's
#     details will be returned.
#     """
#     user_data = user.dict()

#     updated_user = update_user(db, user_id, user_data)

#     if not updated_user:
#         raise HTTPException(status_code=404, detail="User not found or database error")

#     return updated_user

# @router.delete(path="/{user_id}",summary="Delete a user by ID from the database", response_model=UserResponse)
# def delete_user(user_id: int, db: Session = Depends(get_db)):
#     """
#     This endpoint allows you to delete a user from the system using their unique `user_id`. If the user with
#     the specified ID does not exist, or if there is an error during the deletion process, a 404 HTTP exception
#     will be raised. Upon successful deletion, the details of the deleted user will be returned.
#     """
#     deleted_user = delete_users(db, user_id)

#     if not deleted_user:
#         raise HTTPException(status_code=404, detail="User not found or database error")

#     return deleted_user
