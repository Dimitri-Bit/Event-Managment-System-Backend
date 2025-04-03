from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from core.database import get_db
from database.user_role_database import assign_role_to_user  

router = APIRouter(prefix="/user_roles", tags=["User_Roles"])

@router.post(
    path="/", 
    summary="Assign a Role to a User",
    description="This endpoint allows you to assign a specific role to a user by providing the user's ID and the role's ID. It interacts with the database to establish the relationship between the user and the role, ensuring the user receives the correct access permissions or privileges associated with that role."
)
def r_assign_role_to_user(user_id: int, role_id: int, db: Session = Depends(get_db)):
    try:
        return assign_role_to_user(user_id=user_id, role_id=role_id, db=db)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
