from typing import Annotated

from fastapi.params import Depends
from sqlalchemy.orm import Session

from database.connection import get_db

class Base:
    def __init__(self, db: Annotated[Session, Depends(get_db)]):
        self.db = db
