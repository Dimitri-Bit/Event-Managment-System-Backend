from sqlalchemy.exc import SQLAlchemyError
from .base import Base
from model.parties_model import Party
from typing import Sequence, Optional
from sqlalchemy import select

class PartyRepository(Base):
    async def create_parties(self, party: Party) -> Party:
        self.db.add(party)
        await self.db.commit()
        await self.db.flush()
        return party
      
    async def get_all_parties(self,
                              name_party: Optional[str] = None,
                              name_organizer: Optional[str] = None,
                              name_town: Optional[str] = None,
                              name_country: Optional[str] = None,
                              date_start: Optional[str] = None) -> Sequence[Party]:
        try:
            query = select(Party)
            filters = []

            if name_party:
                filters.append(Party.name_party.ilike(f"%{name_party}%"))
            if name_organizer:
                filters.append(Party.name_organizer.ilike(f"%{name_organizer}%"))
            if name_town:
                filters.append(Party.name_town.ilike(f"%{name_town}%"))
            if name_country:
                filters.append(Party.name_country.ilike(f"%{name_country}%"))
            if date_start:
                filters.append(Party.date_start >= date_start)

            if filters:
                query = query.where(*filters)

            result = await self.db.execute(query)
            return result.scalars().all()

        except SQLAlchemyError as e:
            raise e

    async def get_party_by_id(self, party_id: int) -> Optional[Party]:
        try:
            query = select(Party).where(Party.id == party_id)
            result = await self.db.execute(query)
            return result.scalars().first()
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
