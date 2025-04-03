from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.permission import PremCreate, PremResponse
from database.permission_database import create_prem, get_permissions, update_permissions, delete_permissions
from core.database import get_db

router = APIRouter(prefix="/permission", tags=["Permission"])

@router.post("/", summary="Create a new permission", response_model=PremResponse)
def create_permission(prem: PremCreate, db: Session = Depends(get_db)):
    """
    This endpoint allows you to add a new permission entry to the system. The permission will be
    created based on the provided permission data. The system expects the permission data in the
    form of a `PremCreate` schema, which includes necessary attributes for the permission being
    added. Upon successful creation, the new permission's details will be returned as a response.
    """
    return create_prem(db, prem)

@router.get("/", summary="Retrieve all permissions", response_model=list[PremResponse])
def get_all_permissions(db: Session = Depends(get_db)):
    """
    This endpoint retrieves and returns a list of all permissions stored in the system. It is useful
    for administrators or users who need to see the full list of permissions that have been set up in 
    the system. Each permission is represented by a `PremResponse` schema containing details such as 
    the permission name, associated roles, and any other relevant information.
    """
    permissions = get_permissions(db)
    return permissions

@router.put("/{prem_id}", summary="Update an existing permission by ID", response_model=PremResponse)
def update_permission(prem_id: int, prem: PremCreate, db: Session = Depends(get_db)):
    """
    This endpoint allows you to modify an existing permission using its unique identifier (`prem_id`).
    The updated permission data should be provided in the form of a `PremCreate` schema. If the permission
    with the specified ID does not exist, or if there is an error while updating, a 404 HTTP exception 
    will be raised. On success, the updated permission details will be returned.
    """
    prem_data = prem.dict()
    updated_prem = update_permissions(db, prem_id, prem_data)

    if not updated_prem:
        raise HTTPException(status_code=404, detail="Permission not found or database error")

    return updated_prem

@router.delete("/{prem_id}", summary="Delete a permission by ID", response_model=PremResponse)
def delete_permission(prem_id: int, db: Session = Depends(get_db)):
    """
    This endpoint allows you to delete a permission from the system using its unique identifier (`prem_id`).
    If the permission with the specified ID does not exist, or if there is an error during the deletion,
    a 404 HTTP exception will be raised. Upon successful deletion, the details of the removed permission
    will be returned as a response.
    """
    deleted_prem = delete_permissions(db, prem_id)

    if not deleted_prem:
        raise HTTPException(status_code=404, detail="Permission not found or database error")

    return deleted_prem
