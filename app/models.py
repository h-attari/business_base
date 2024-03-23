"""
This module contains the table models/structure required for the application.
"""
from sqlalchemy import Column, Integer, String

from app.database import BASE


class Business(BASE):
    """
    Business model class using SQLAlchemy Base to create
    the Business table in the database.
    """

    __tablename__ = "Businesses"

    id = Column(Integer, primary_key=True, autoincrement="auto")
    name = Column(String(256), unique=True)
    address = Column(String(256))
    owner = Column(String(256))
    employee_size = Column(Integer, default=0)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name
