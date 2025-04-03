from sqlalchemy.orm import Session
from models.user import User
from schemas.user import UserCreate
from core.security import hash_password
from sqlalchemy.exc import SQLAlchemyError

def create_user(db: Session, user: UserCreate):
    hashed_password = hash_password(user.password)
    db_user = User(username=user.username, email=user.email, password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_users(db: Session):
    try:
        return db.query(User).all() 
    except Exception as e:
        print(f"Error fetching roles: {e}")
        raise e

def update_user(db: Session, user_id: int, user_data: dict):
    try:
        
        user = db.query(User).filter(User.id == user_id).first()

        if not user:
            return None  


        for key, value in user_data.items():
            setattr(user, key, value)

        db.commit()  
        db.refresh(user) 
        return user 
    except SQLAlchemyError as e:
        print(f"Database error occurred: {e}")  
        return None


def delete_users(db: Session, user_id: int):
    try:
        print(f"Attempting to delete user with ID: {user_id}")
        user = db.query(User).filter(User.id == user_id).first()
        
        if not user:
            return None
        
        db.delete(user)
        db.commit()
        return user
    except SQLAlchemyError as e:
        print(f"Database error occurred: {e}")
        return None