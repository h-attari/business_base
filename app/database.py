"""
This module contains the database configuration for the project.
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine("sqlite:///business.db")

BASE = declarative_base()

SessionLocal = sessionmaker(bind=engine, expire_on_commit=False)


def get_session():
    """
    This method is used to create and return a database session.
    """
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()
