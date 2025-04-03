from sqlalchemy.exc import SQLAlchemyError
from .base import Base
from model.user_model import User

class UserRepository(Base):

    def create_user(self, user: User) -> User:
        self.db.add(user);
        self.db.commit();
        self.db.flush();
        return user;


    def get_users(self):
        try:
            return self.db.query(User).all()
        except Exception as e:
            print(f"Error fetching roles: {e}")
            raise e


    def delete_users(self, user_id: int):
        try:
            print(f"Attempting to delete user with ID: {user_id}")
            user = self.db.query(User).filter(User.id == user_id).first()

            if not user:
                return None

            self.db.delete(user)
            self.db.commit()
            return user
        except SQLAlchemyError as e:
            print(f"Database error occurred: {e}")
            raise e
