from sqlalchemy.exc import SQLAlchemyError
from .base import Base
from model.parties_model import Party
from typing import List, Sequence
from sqlalchemy import select

class PartyRepository(Base):
    async def create_parties(self, party: Party) -> Party:
        self.db.add(party)
        await self.db.commit()
        await self.db.flush()
        return party

    async def get_all_parties(self) -> List[Party]:
        try:
            result = await self.db.execute(select(Party))
            parties: Sequence[Party] = result.scalars().all()
            return list(parties)
        except SQLAlchemyError as e:
            raise e

    async def update_party(self, party_id: int, update_data: dict) -> Party:
        try:
            result = await self.db.execute(select(Party).filter(Party.id == party_id))
            db_party = result.scalars().first()
            if not db_party:
                raise ValueError("Party not found")

            for key, value in update_data.items():
                setattr(db_party, key, value)

            self.db.add(db_party)
            await self.db.commit()
            await self.db.refresh(db_party)
            return db_party
        except SQLAlchemyError as e:
            await self.db.rollback()
            raise e

    async def delete_party(self, party_id: int) -> None:
        try:
            result = await self.db.execute(select(Party).filter(Party.id == party_id))
            party = result.scalars().first()
            if not party:
                raise ValueError("Party not found")

            await self.db.delete(party)
            await self.db.commit()
        except SQLAlchemyError as e:
            await self.db.rollback()
            raise e
