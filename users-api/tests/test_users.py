import uuid
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_create_user():
    user_id = str(uuid.uuid4())
    payload = {
        "id": user_id,
        "name": "Test User",
        "email": "test@example.com",
        "age": 25
    }
    response = client.post("/users/", json=payload)
    assert response.status_code == 200
    assert response.json()["name"] == "Test User"


def test_get_users_list():
    response = client.get("/users/")
    assert response.status_code in (200, 404)


def test_get_nonexistent_user():
    fake_id = str(uuid.uuid4())
    response = client.get(f"/users/{fake_id}")
    assert response.status_code == 404


def test_update_user():
    user_id = str(uuid.uuid4())
    create_payload = {
        "id": user_id,
        "name": "Original Name",
        "email": "original@example.com",
        "age": 30
    }
    client.post("/users/", json=create_payload)

    update_payload = {
        "id": user_id,
        "name": "Updated Name",
        "email": "updated@example.com",
        "age": 31
    }
    response = client.put(f"/users/{user_id}", json=update_payload)
    assert response.status_code == 200
    assert response.json()["name"] == "Updated Name"


def test_delete_user():
    user_id = str(uuid.uuid4())
    create_payload = {
        "id": user_id,
        "name": "ToDelete",
        "email": "delete@example.com",
        "age": 40
    }
    client.post("/users/", json=create_payload)

    response = client.delete(f"/users/{user_id}")
    assert response.status_code == 200
    assert response.json() is True
