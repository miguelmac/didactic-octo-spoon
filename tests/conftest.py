import pytest
from fastapi.testclient import TestClient
from src.app import app

@pytest.fixture
def client():
    return TestClient(app)

@pytest.fixture
def sample_email():
    return "test.student@mergington.edu"

@pytest.fixture
def valid_activity_names():
    return [
        "Chess Club",
        "Programming Class",
        "Gym Class",
        "Basketball Team",
        "Tennis Club",
        "Art Studio",
        "Drama Club",
        "Science Club",
        "Debate Team"
    ]