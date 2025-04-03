from fastapi import APIRouter, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session
from schemas.parties import PartyCreate, PartyUpdate, PartyResponse
from services.parties_service import PartiesService
from typing import Annotated


router = APIRouter(prefix="/parties", tags=["Parties"])

@router.post("/", response_model=PartyResponse)
def create_party(
    party_data: PartyCreate,
    service: Annotated[PartiesService, Depends(PartiesService)]
):
    db_party = service.create_party(party_data)
    return PartyResponse.model_validate(db_party)


# @router.get("/{party_id}", response_model=PartyResponse)
# def read_party(party_id: int, service: Annotated[PartiesService, Depends(PartiesService)]):
#     party = service.get_party(party_id)
#     if not party:
#         raise HTTPException(status_code=404, detail="Party not found")
#     return party

# @router.get("/", response_model=List[PartyResponse])
# def read_parties(service: Annotated[PartiesService, Depends(PartiesService)], skip: int = 0, limit: int = 10):
#     return service.get_all_parties(skip, limit)

# @router.put("/{party_id}", response_model=PartyResponse)
# def update_party(party_id: int, party_data: PartyUpdate, service: Annotated[PartiesService, Depends(PartiesService)]):
#     updated_party = service.update_party(party_id, party_data)
#     if not updated_party:
#         raise HTTPException(status_code=404, detail="Party not found")
#     return updated_party

# @router.delete("/{party_id}", response_model=PartyResponse)
# def delete_party(party_id: int, service: Annotated[PartiesService, Depends(PartiesService)]):
#     deleted_party = service.delete_party(party_id)
#     if not deleted_party:
#         raise HTTPException(status_code=404, detail="Party not found")
#     return deleted_party
