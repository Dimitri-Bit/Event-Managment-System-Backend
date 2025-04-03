from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import settings
import discover_models
discover_models.import_models();

db_url = settings.settings.db_url;

engine = create_engine(
    db_url,
    pool_pre_ping=True,
    echo=True
);

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine);

def get_db():
    db = SessionLocal();
    try:
        yield db;
    finally:
        db.close();
