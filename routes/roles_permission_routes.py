from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from core.database import get_db
from database.role_permission_database import assign_permission_to_role

router = APIRouter(prefix="/role_permissions", tags=["Role_Permissions"])

@router.post(path = "/", summary="Assign Permission to a Role")
def assign_permission(role_id: int, permission_id: int, db: Session = Depends(get_db)):
    '''
     This endpoint assigns a specific permission to a role by updating the database with the provided role ID and permission ID. It takes the role ID and permission ID as input, and the database session is used to perform the necessary updates.
    '''
    return assign_permission_to_role(role_id, permission_id, db)

