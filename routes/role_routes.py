from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.role import RoleCreate, RoleResponse
from database.role_database import create_role, get_roles, update_role, delete_roles
from core.database import get_db

router = APIRouter(prefix="/role", tags=["Roles"])

@router.post(path="/",summary='Create a new role in the database', response_model=RoleResponse)
def create_roles(role: RoleCreate, db: Session = Depends(get_db)):
    """
    This endpoint allows you to create a new role with the specified details. You must provide the role data
    in the form of a `RoleCreate` schema, which includes attributes like the role name and its associated permissions.
    Upon successful creation, the newly created role will be returned with the role's data.
    """
    return create_role(db, role)

@router.get(path="/",summary="Retrieve all roles from the database", response_model=list[RoleResponse])
def get_all_roles(db: Session = Depends(get_db)):
    """
    This endpoint returns a list of all roles stored in the system. Each role is represented as a `RoleResponse` schema
    containing the role name, associated permissions, and any other relevant information. This endpoint is useful for
    administrators or users who need to view all available roles.
    """
    roles = get_roles(db)
    return roles

@router.put(path="/{role_id}",summary="Update an existing role by ID", response_model=RoleResponse)
def update_role(role_id: int, role: RoleCreate, db: Session = Depends(get_db)):
    """

    This endpoint allows you to modify an existing role identified by its unique `role_id`. You must provide the updated
    role data in the form of a `RoleCreate` schema. If the role with the specified ID does not exist or if there is an
    error while updating the role, a 404 HTTP exception will be raised. On success, the updated role details will be returned.
    """
    role_data = role.dict()

    updated_role = update_role(db, role_id, role_data)

    if not updated_role:
        raise HTTPException(status_code=404, detail="Role not found or database error")

    return updated_role

@router.delete(path="/{role_id}",summary=" Delete a role by ID", response_model=RoleResponse)
def delete_role(role_id: int, db: Session = Depends(get_db)):
    """

    This endpoint allows you to delete a role identified by its unique `role_id`. If the role does not exist or there is
    an error during the deletion process, a 404 HTTP exception will be raised. Upon successful deletion, the details of
    the deleted role will be returned.
    """
    deleted_role = delete_roles(db, role_id)

    if not deleted_role:
        raise HTTPException(status_code=404, detail="Role not found or database error")

    return deleted_role
