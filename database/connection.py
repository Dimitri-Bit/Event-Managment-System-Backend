from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model.base import Base
from model.permission_model import Permission
from model.role_model import Role
from model.user_model import User
from model.permission_role import permission_role
from model.parties_model import Party
import os
from dotenv import load_dotenv

load_dotenv();
db_url = os.getenv("DB_URL");
if (db_url is None):
    db_url = "sqlite:///db.db";

engine = create_engine(
    db_url,
    pool_pre_ping=True,
    echo=True
);
# Base.metadata.create_all(engine);
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine);

def get_db():
    db = SessionLocal();
    try:
        yield db;
    finally:
        db.close();
