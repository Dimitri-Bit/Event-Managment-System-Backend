from typing import Annotated
from fastapi import Depends
from model.parties_model import Party
from repository.parties_repository import PartyRepository
from schemas.parties import PartyCreate, PartyUpdate, PartyResponse

class PartiesService:
    def __init__(self, repository: Annotated[PartyRepository, Depends(PartyRepository)]):
        self.repository = repository

    def create_party(self, party_data: PartyCreate):
        db_party = self.map_create_party(party_data)
        return self.repository.create_party(db_party)

    # def get_party(self, party_id: int):
    #     return self.repository.get_party(party_id)

    # def get_all_parties(self, skip: int = 0, limit: int = 10):
    #     return self.repository.get_all_parties(skip, limit)

    # def update_party(self, party_id: int, party_data: PartyUpdate):
    #     return self.repository.update_party(party_id, party_data)

    # def delete_party(self, party_id: int):
    #     return self.repository.delete_party(party_id)

    def map_create_party(self, create_request: PartyCreate) -> Party:
     return Party(
        name_party=create_request.name_party,
        url_image_full=create_request.url_image_full,
        name_organizer=create_request.name_organizer,
        date_start=create_request.date_start,
        date_end=create_request.date_end,
        name_town=create_request.name_town,
        name_country=create_request.name_country,
        name_type=create_request.name_type,
        text_entry_fee=create_request.text_entry_fee,
        text_more=create_request.text_more,
        url_organizer=create_request.url_organizer,
        url_party=create_request.url_party
     )
