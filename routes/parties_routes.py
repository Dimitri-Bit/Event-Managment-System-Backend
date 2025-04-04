from typing import Annotated, List,Optional

from fastapi import APIRouter, HTTPException, status, Depends,Query
from fastapi.responses import Response

from schemas.parties import PartyCreate, PartyUpdate, PartyResponse
from services.parties_service import PartiesService

router = APIRouter(prefix="/party", tags=["Party"])


#create party
@router.post(
    path="/",
    summary="Register a new party",
    description="""
    This endpoint allows users to register a new party in the database.  
    It accepts party details as input and returns the created party data.
    """,
    response_model=PartyResponse
)
def register_party(party: PartyCreate, service: Annotated[PartiesService, Depends(PartiesService)]):
    return service.add_party(party)


# get parties
@router.get(
    path="/",
    summary="Retrieve all parties",
    description="""
    This endpoint fetches all registered parties from the database.  
    It returns a list of parties with their respective details.
    """,
    response_model=List[PartyResponse]
)
def get_all_parties(service: Annotated[PartiesService, Depends(PartiesService)]):
    return service.get_all_parties()

#filtering parties
@router.get(
    path="/filter",
    summary="Filter parties by different fields",
    description="""This endpoint allows users to filter parties based on multiple criteria such as party name, organizer, town, country, and start date.  
    Users can specify one or more parameters to filter the results:
    - `name_party`: The name of the party.
    - `name_organizer`: The name of the organizer.
    - `name_town`: The town where the party is being held.
    - `name_country`: The country where the party is taking place.
    - `date_start`: The start date of the party in `YYYY-MM-DD` format.
    
    If no filters are provided, all parties will be returned.""",
    response_model=List[PartyResponse]
)
def filter_parties(
    service: Annotated[PartiesService, Depends(PartiesService)],
    name_party: Optional[str] = Query(None, description="Filter by party name"),
    name_organizer: Optional[str] = Query(None, description="Filter by organizer name"),
    name_town: Optional[str] = Query(None, description="Filter by town"),
    name_country: Optional[str] = Query(None, description="Filter by country"),
    date_start: Optional[str] = Query(None, description="Filter by start date (YYYY-MM-DD)")
):
    try:
        return service.get_filtered_parties(name_party, name_organizer, name_town, name_country, date_start)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))




# get party by id
@router.get(
    path="/{party_id}",
    summary="Retrieve a party by ID",
    description="""
    This endpoint fetches a specific party using its ID.  
    If the party ID does not exist, it returns a 404 error.
    """,
    response_model=PartyResponse
)
def get_party_by_id(party_id: int, service: Annotated[PartiesService, Depends(PartiesService)]):
    party = service.get_party_by_id(party_id)
    if not party:
        raise HTTPException(status_code=404, detail="Party not found")
    return party

    


#update party
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

  
#delete party
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
def delete_party(party_id: int, service: PartiesService = Depends(PartiesService)):
    try:
        service.delete_party(party_id)
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))

