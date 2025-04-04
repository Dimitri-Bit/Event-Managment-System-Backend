from typing import Annotated, List
from fastapi import APIRouter, HTTPException, status, Depends
from fastapi.responses import Response
from schemas.parties import PartyCreate, PartyUpdate, PartyResponse
from services.parties_service import PartiesService

router = APIRouter(prefix="/party", tags=["Party"])

@router.post(
    path="/",
    summary="Register a new party",
    description="""
    This endpoint allows users to register a new party in the database.
    It accepts party details as input and returns the created party data.
    """,
    response_model=PartyResponse
)
async def register_party(party: PartyCreate, service: Annotated[PartiesService, Depends(PartiesService)]):
    return await service.add_party(party)

@router.get(
    path="/",
    summary="Retrieve all parties",
    description="""
    This endpoint fetches all registered parties from the database.
    It returns a list of parties with their respective details.
    """,
    response_model=List[PartyResponse]
)
async def get_all_parties(service: Annotated[PartiesService, Depends(PartiesService)]):
    return await service.get_all_parties()

@router.put(
    path="/{party_id}",
    summary="Update an existing party",
    description="""
    This endpoint updates an existing party's details based on the provided party ID.
    It accepts partial updates, meaning only the provided fields will be changed.

    - If the party ID does not exist, it returns a 404 error.
    """,
    response_model=PartyResponse
)
async def update_party(
    party_id: int,
    update_request: PartyUpdate,
    service: Annotated[PartiesService, Depends(PartiesService)]
):
    try:
        updated_party = await service.update_party(party_id, update_request.dict(exclude_unset=True))
        return updated_party
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.delete(
    path="/{party_id}",
    summary="Delete a party",
    description="""
    This endpoint deletes a party based on the provided party ID.
    If the party ID is not found, it raises a 404 error.

    - Successful deletion returns a 204 No Content response.
    """,
    status_code=status.HTTP_204_NO_CONTENT
)
async def delete_party(party_id: int, service: Annotated[PartiesService, Depends(PartiesService)]):
    try:
        await service.delete_party(party_id)
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
