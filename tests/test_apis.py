"""
This module contains the test cases for the application APIs.
"""
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.database import get_session
from app.main import app

engine = create_engine("sqlite:///test.db")


TestSessionLocal = sessionmaker(bind=engine, expire_on_commit=False)


def overide_get_session():
    """
    This method overides the default DB session to use the the Test Session.
    """
    try:
        session = TestSessionLocal()
        yield session
    finally:
        session.close()


app.dependency_overrides[get_session] = overide_get_session


client = TestClient(app)


def test_create_business_success(test_db, business_data):
    """
    Test case to successfully create a new database record in the application.
    """
    resp = client.post("/business", json=business_data[0])
    assert resp.status_code == 201
    assert resp.json() == {
        "id": 1,
        "name": business_data[0]["business_name"],
        "address": business_data[0]["address"],
        "owner": business_data[0]["business_owner"],
        "employee_size": business_data[0]["employee_size"],
    }
    resp = client.post("/business", json=business_data[1])
    assert resp.status_code == 201
    assert resp.json() == {
        "id": 2,
        "name": business_data[1]["business_name"],
        "address": business_data[1]["address"],
        "owner": business_data[1]["business_owner"],
        "employee_size": business_data[1]["employee_size"],
    }


def test_create_business_failure(test_db, business_data):
    """
    Failure test case to create a new database record in the application.
    """
    resp = client.post("/business", json=business_data[1])
    assert resp.status_code == 400
    assert resp.json() == {
        "detail": f"Business with name '{business_data[1]['business_name']}' already exists!"
    }


def test_search_business_success(test_db, business_data):
    """
    Test case to successfully search an existing record in the database.
    """
    resp = client.get("/business")
    assert resp.status_code == 200
    assert resp.json() == [
        {
            "id": 1,
            "name": business_data[0]["business_name"],
            "address": business_data[0]["address"],
            "owner": business_data[0]["business_owner"],
            "employee_size": business_data[0]["employee_size"],
        },
        {
            "id": 2,
            "name": business_data[1]["business_name"],
            "address": business_data[1]["address"],
            "owner": business_data[1]["business_owner"],
            "employee_size": business_data[1]["employee_size"],
        },
    ]
    resp = client.get(
        "/business", params={"business_name": business_data[0]["business_name"]}
    )
    assert resp.status_code == 200
    assert resp.json() == {
        "id": 1,
        "name": business_data[0]["business_name"],
        "address": business_data[0]["address"],
        "owner": business_data[0]["business_owner"],
        "employee_size": business_data[0]["employee_size"],
    }


def test_search_business_failure(test_db):
    """
    Failure test case to search an existing record in the database.
    """
    resp = client.get("/business", params={"business_name": "Third Business"})
    assert resp.status_code == 404
    assert resp.json() == {"detail": "Requested business not found!"}


def test_update_business_success(test_db, update_business_data):
    """
    Test case to successfully update an existing record in the database.
    """
    resp = client.put("/business/1", json=update_business_data)
    assert resp.status_code == 200
    assert resp.json() == {
        "id": 1,
        "name": update_business_data["business_name"],
        "address": update_business_data["address"],
        "owner": update_business_data["business_owner"],
        "employee_size": update_business_data["employee_size"],
    }


def test_update_business_failure(test_db, update_business_data):
    """
    Failure test case to update an existing record in the database.
    """
    resp = client.put("/business/3", json=update_business_data)
    assert resp.status_code == 404
    assert resp.json() == {"detail": "Requested business not found!"}


def test_delete_business_success(test_db):
    """
    Test case to successfully delete an existing record in the database.
    """
    resp = client.delete("/business/2")
    assert resp.status_code == 204


def test_delete_business_failure(test_db):
    """
    Failure test case to delete an existing record in the database.
    """
    resp = client.delete("/business/2")
    assert resp.status_code == 404
    assert resp.json() == {"detail": "Requested business not found!"}
