from sqlalchemy.exc import SQLAlchemyError
from .base import Base
from model.parties_model import Party
from typing import List,Optional

class PartyRepository(Base):
    def create_parties(self, party: Party) -> Party:
        self.db.add(party)
        self.db.commit()
        self.db.flush()
        return party

    def get_all_parties(self, 
                        name_party: Optional[str] = None, 
                        name_organizer: Optional[str] = None, 
                        name_town: Optional[str] = None,
                        name_country: Optional[str] = None, 
                        date_start: Optional[str] = None) -> List[Party]:
        try:
            query = self.db.query(Party)

            # Apply filters if provided
            if name_party:
                query = query.filter(Party.name_party.ilike(f"%{name_party}%"))
            if name_organizer:
                query = query.filter(Party.name_organizer.ilike(f"%{name_organizer}%"))
            if name_town:
                query = query.filter(Party.name_town.ilike(f"%{name_town}%"))
            if name_country:
                query = query.filter(Party.name_country.ilike(f"%{name_country}%"))
            if date_start:
                query = query.filter(Party.date_start >= date_start)

            return query.all()
        except SQLAlchemyError as e:
            raise e
            

    def get_party_by_id(self, party_id: int) -> Party:
        try:
            return self.db.query(Party).filter(Party.id == party_id).first()
        except SQLAlchemyError as e:
            raise e

    def update_party(self, party_id: int, update_data: dict) -> Party:
        try:
            db_party = self.db.query(Party).filter(Party.id == party_id).first()
            if not db_party:
                raise ValueError("Party not found")
            
           
            for key, value in update_data.items():
                setattr(db_party, key, value)

            self.db.add(db_party)
            self.db.commit()
            self.db.refresh(db_party)
            return db_party
        except SQLAlchemyError as e:
            self.db.rollback()
            raise e

    def delete_party(self, party_id: int) -> None:
        try:
            party = self.db.query(Party).filter(Party.id == party_id).first()
            if not party:
                raise ValueError("Party not found")
            self.db.delete(party)
            self.db.commit()
        except SQLAlchemyError as e:
            self.db.rollback()
            raise e
