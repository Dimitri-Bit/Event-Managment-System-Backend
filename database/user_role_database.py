from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models.user import User
from models.role import Role
from models.user_role import UserRole
from core.database import get_db


def assign_role_to_user(user_id: int, role_id: int, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.id == user_id).first()
    db_role = db.query(Role).filter(Role.id == role_id).first()

    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    
    if not db_role:
        raise HTTPException(status_code=404, detail="Role not found")

    user_role = UserRole(user_id=user_id, role_id=role_id)
    db.add(user_role)
    db.commit()
    return {"message": "Role assigned to user successfully"}