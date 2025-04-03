from sqlalchemy.orm import Session
from model.parties_model import Party
from schemas.parties import PartyCreate, PartyUpdate, PartyResponse

class PartyRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_party(self, party_data: Party) -> Party:
        self.db.add(party_data)
        self.db.commit()
        self.db.refresh(party_data)
        return party_data

    # def get_party(self, party_id: int):
    #     party = self.db.query(Party).filter(Party.id == party_id).first()
    #     if party:
    #         return party
    #     return None

    # def get_all_parties(self, skip: int = 0, limit: int = 10):
    #     return self.db.query(Party).offset(skip).limit(limit).all()

    # def update_party(self, party_id: int, party_data: Party):
    #     db_party = self.db.query(Party).filter(Party.id == party_id).first()
    #     if not db_party:
    #         return None
    #     for key, value in party_data.dict(exclude_unset=True).items():
    #         setattr(db_party, key, value)
    #     self.db.commit()
    #     self.db.refresh(db_party)
    #     return db_party

    # def delete_party(self, party_id: int):
    #     db_party = self.db.query(Party).filter(Party.id == party_id).first()
    #     if not db_party:
    #         return None
    #     self.db.delete(db_party)
    #     self.db.commit()
    #     return db_party
