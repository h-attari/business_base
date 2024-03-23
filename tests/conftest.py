"""
This module contains the pytest fixtures for the test cases.
"""
import os

import pytest
from faker import Faker

from app.database import BASE
from tests.test_apis import engine

fake = Faker()


@pytest.fixture(scope="session")
def test_db():
    """
    This fixture creates and drops the test database tables.
    """
    BASE.metadata.create_all(bind=engine)
    yield
    BASE.metadata.drop_all(bind=engine)
    try:
        os.remove("test.db")
    except FileNotFoundError as e:
        print(f"File not Found: {e}")


@pytest.fixture(scope="session")
def business_data():
    """
    This fixture creates the fake business data to save and query from database..
    """
    data = []
    for _ in range(2):
        data.append(
            {
                "business_name": fake.company(),
                "address": fake.city(),
                "business_owner": fake.name(),
                "employee_size": fake.random_int(min=5, max=1000000),
            }
        )
    return data


@pytest.fixture
def update_business_data():
    """
    This fixture returns the fake busines payload for update API.
    """
    return {
        "business_name": fake.company(),
        "address": fake.city(),
        "business_owner": fake.name(),
        "employee_size": fake.random_int(min=5, max=1000000),
    }
