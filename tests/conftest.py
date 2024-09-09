import pytest
from fastapi.testclient import TestClient

from duzero_fastapi.app import app


@pytest.fixture
def client():
    return TestClient(app)
