from typing import Annotated

from fastapi import APIRouter,HTTPException
from fastapi.params import Depends
from typing import List
from fastapi import status
from fastapi.responses import Response

from schemas.parties import PartyCreate,PartyUpdate
from services.parties_service import PartiesService
from schemas.parties import PartyResponse

router = APIRouter(prefix="/party", tags=["Party"])


@router.post(path="/",summary=" Register a new user in the database", response_model=PartyResponse)
def register_user(party: PartyCreate, service: Annotated[PartiesService, Depends(PartiesService)]):

    return service.add_party(party);


@router.get(path="/",summary=" Register a new user in the database", response_model=List[PartyResponse])
def register_user(service: Annotated[PartiesService, Depends(PartiesService)]):

    return service.get_all_parties()

@router.put("/{party_id}", summary="Update a party", response_model=PartyResponse)
def update_party(
    party_id: int,
    update_request: PartyUpdate,
    service: Annotated[PartiesService, Depends(PartiesService)]
):
    try:
        updated_party = service.update_party(party_id, update_request.dict(exclude_unset=True))
        return updated_party
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.delete("/{party_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_party(party_id: int, service: PartiesService = Depends(PartiesService)):
    try:
        service.delete_party(party_id)
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))