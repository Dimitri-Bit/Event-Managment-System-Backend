from typing import Annotated

from fastapi.params import Depends
from repository.parties_repository import PartyRepository

from schemas.parties import PartyCreate
from model.parties_model import Party

class PartiesService:
    def __init__(self, repository: Annotated[PartyRepository, Depends(PartyRepository)]):
        self.repository = repository

    def add_party(self, create_request: PartyCreate) -> Party:
        db_party = self.map_create_party(create_request)
        return self.repository.create_parties(db_party)

    def get_all_parties(self) -> list[Party]:
        return self.repository.get_all_parties()
    
    def update_party(self, party_id: int, update_request: dict) -> Party:
        return self.repository.update_party(party_id, update_request)

    def delete_party(self, party_id: int) -> None:
        self.repository.delete_party(party_id)


    def map_create_party(self,party_request: PartyCreate) -> Party:
      return Party(
        name_party=party_request.name_party,
        url_image_full=party_request.url_image_full,
        name_organizer=party_request.name_organizer,
        date_start=party_request.date_start,
        date_end=party_request.date_end,
        name_town=party_request.name_town,
        name_country=party_request.name_country,
        name_type=party_request.name_type,
        text_entry_fee=party_request.text_entry_fee,
        text_more=party_request.text_more,
        url_organizer=party_request.url_organizer,
        url_party=party_request.url_party
    )
    