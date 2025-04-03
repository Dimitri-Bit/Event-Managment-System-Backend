from sqlalchemy.orm import Session
from models.permission import Permission
from schemas.permission import PremCreate
from sqlalchemy.exc import SQLAlchemyError

def create_prem(db: Session, prem: PremCreate):
    db_prem = Permission(name=prem.name, description=prem.description)
    db.add(db_prem)
    db.commit()
    db.refresh(db_prem)
    return db_prem

def get_permissions(db: Session):
    try:
        return db.query(Permission).all() 
    except Exception as e:
        print(f"Error fetching roles: {e}")
        raise e


def update_permissions(db: Session, prem_id: int, prem_data: dict):
    try:
        prem = db.query(Permission).filter(Permission.id == prem_id).first()

        if not prem:
            return None  


        for key, value in prem_data.items():
            setattr(prem, key, value)

        db.commit()  
        db.refresh(prem) 
        return prem  
    except SQLAlchemyError as e:
        print(f"Database error occurred: {e}")  
        return None

def delete_permissions(db: Session, prem_id: int):
    try:
        print(f"Attempting to delete prem with ID: {prem_id}")
        prem = db.query(Permission).filter(permission.id == prem_id).first()
        
        if not prem:
            return None
        
        db.delete(prem)
        db.commit()
        return prem
    except SQLAlchemyError as e:
        print(f"Database error occurred: {e}")
        return None