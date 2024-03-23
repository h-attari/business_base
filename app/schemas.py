"""
This module contains the request and response schemase required for the apis.
"""
from typing import Optional

from pydantic import BaseModel


class CreateBusinessSchema(BaseModel):
    """
    This is the schema class which defines the requst schema
    required to create a new business record.
    """

    business_name: str
    address: str
    business_owner: str
    employee_size: int


class UpdateBusinessSchema(BaseModel):
    """
    This is the schema class which defines the requst schema
    required to update an existing business record.
    """

    business_name: Optional[str] = None
    address: Optional[str] = None
    business_owner: Optional[str] = None
    employee_size: Optional[int] = None


class BusinessSchema(BaseModel):
    """
    This is the schema class which defines the response class
    required to return a proper structure response for the apis.
    """

    id: int
    name: str
    address: str
    owner: str
    employee_size: int
