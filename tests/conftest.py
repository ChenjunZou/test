import pytest

from app import create_app


@pytest.fixture
def app():
    """Create application for testing."""
    app = create_app({"TESTING": True, "SECRET_KEY": "test-secret"})
    yield app


@pytest.fixture
def client(app):
    """Create a test client."""
    return app.test_client()
