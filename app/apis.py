"""
This module contains the apis and api-endpoints
required for the working of the application.
"""
from typing import List, Union

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database import get_session
from app.models import Business
from app.schemas import BusinessSchema, CreateBusinessSchema, UpdateBusinessSchema

router = APIRouter(prefix="/business")


@router.post("", status_code=status.HTTP_201_CREATED, response_model=BusinessSchema)
async def create_business(
    business: CreateBusinessSchema, session: Session = Depends(get_session)
):
    """
    Create API to create a new business record.
    """
    if session.query(Business).filter_by(name=business.business_name).first():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Business with name '{business.business_name}' already exists!"
        )
    business_obj = Business(
        name=business.business_name,
        address=business.address,
        owner=business.business_owner,
        employee_size=business.employee_size,
    )
    session.add(business_obj)
    session.commit()
    return business_obj


@router.get(
    "",
    status_code=status.HTTP_200_OK,
    response_model=Union[BusinessSchema, List[BusinessSchema]],
)
async def search_business(
    business_name: str = None, session: Session = Depends(get_session)
):
    """
    Get API to return an existing business record or list of business records.
    """
    if business_name is not None:
        business_obj = session.query(Business).filter_by(name=business_name).first()
        if business_obj is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Requested business not found!"
            )
    else:
        business_obj = session.query(Business).all()
    return business_obj


@router.put(
    "/{business_id}", status_code=status.HTTP_200_OK, response_model=BusinessSchema
)
async def update_business(
    business_id: int,
    business: UpdateBusinessSchema,
    session: Session = Depends(get_session),
):
    """
    Update API to update an existing business record.
    """
    business_obj = session.get(Business, business_id)
    if business_obj is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Requested business not found!"
        )
    if business.business_name:
        business_obj.name = business.business_name
    if business.address:
        business_obj.address = business.address
    if business.business_owner:
        business_obj.owner = business.business_owner
    if business.employee_size:
        business_obj.employee_size = business.employee_size
    session.commit()
    return business_obj


@router.delete("/{business_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_business(business_id: int, session: Session = Depends(get_session)):
    """
    Delete API to delete an existing business record.
    """
    business_obj = session.get(Business, business_id)
    if business_obj is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Requested business not found!"
        )
    session.delete(business_obj)
    session.commit()
    return None
