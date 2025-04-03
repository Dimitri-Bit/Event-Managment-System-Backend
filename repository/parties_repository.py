from sqlalchemy.exc import SQLAlchemyError
from .base import Base
from model.parties_model import Party
from typing import List

class PartyRepository(Base):
    def create_parties(self, party: Party) -> Party:
        self.db.add(party)
        self.db.commit()
        self.db.flush()
        return party

    def get_all_parties(self) -> List[Party]:
        try:
            return self.db.query(Party).all()
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