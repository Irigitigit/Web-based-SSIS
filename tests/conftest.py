import pytest
from flask_jwt_extended import create_access_token
from ssis import create_app

@pytest.fixture
def app():
    app = create_app()
    app.config.update({
        "TESTING": True,
        "SECRET_KEY": "test_secret",
        "JWT_SECRET_KEY": "test_secret"
    })
    yield app

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def auth_headers(app):
    with app.app_context():
        # Use a simple string identity instead of a dict to fix 422 error
        token = create_access_token(identity="test_user")
        return {"Authorization": f"Bearer {token}"}
