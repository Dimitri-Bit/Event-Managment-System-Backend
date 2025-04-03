from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models.role import Role
from models.permission import Permission
from models.role_permission import RolePermission
from core.database import get_db

def assign_permission_to_role(role_id: int, permission_id: int, db: Session = Depends(get_db)):

    db_role = db.query(Role).filter(Role.id == role_id).first()
    db_permission = db.query(Permission).filter(Permission.id == permission_id).first()


    if not db_role:
        raise HTTPException(status_code=404, detail="Role not found")

    if not db_permission:
        raise HTTPException(status_code=404, detail="Permission not found")

 
    role_permission = RolePermission(role_id=role_id, permission_id=permission_id)
    db.add(role_permission)
    db.commit()
    return {"message": "Permission assigned to role successfully"}
