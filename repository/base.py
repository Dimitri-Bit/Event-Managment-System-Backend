from typing import Annotated
from fastapi.params import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from database.database import get_db_session

class Base:
    def __init__(self, db: Annotated[AsyncSession, Depends(get_db_session)]):
        self.db = db
