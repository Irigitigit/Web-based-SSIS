import pytest
from ssis import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

@pytest.fixture
def auth_client(client):
    login = client.post("/api/login", json={"username": "miko", "password": "pogiako123"})
    token = login.get_json()["access_token"]
    client.environ_base['HTTP_AUTHORIZATION'] = f"Bearer {token}"
    return client
