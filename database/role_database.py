from sqlalchemy.orm import Session
from models.role import Role
from schemas.role import RoleCreate
from sqlalchemy.exc import SQLAlchemyError

def create_role(db: Session, role: RoleCreate):
    db_role = Role(name=role.name, description=role.description)
    db.add(db_role)
    db.commit()
    db.refresh(db_role)
    return db_role

def get_roles(db: Session):
    try:
        return db.query(Role).all() 
    except Exception as e:
        print(f"Error fetching roles: {e}")
        raise e


def update_role(db: Session, role_id: int, role_data: dict):
    try:
        role = db.query(Role).filter(Role.id == role_id).first()

        if not role:
            return None  


        for key, value in role_data.items():
            setattr(role, key, value)

        db.commit()  
        db.refresh(role) 
        return role  
    except SQLAlchemyError as e:
        print(f"Database error occurred: {e}")  
        return None

def delete_roles(db: Session, role_id: int):
    try:
        print(f"Attempting to delete role with ID: {role_id}")
        role = db.query(Role).filter(Role.id == role_id).first()
        
        if not role:
            return None
        
        db.delete(role)
        db.commit()
        return role
    except SQLAlchemyError as e:
        print(f"Database error occurred: {e}")
        return None