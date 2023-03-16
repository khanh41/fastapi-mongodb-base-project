"""User Authentication Unit Test."""
from __future__ import annotations

from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_login_error():
    """Test login error."""
    response = client.get("/login")
    assert response.status_code == 401

    response = client.post("/token")
    assert response.status_code == 422

    response = client.post("/docs")
    assert response.status_code == 405

    response = client.get("/users/me")
    assert response.status_code == 403


def test_logout_success():
    """Test login error."""
    response = client.get("")
    assert response.status_code == 200

    response = client.get("/logout")
    assert response.status_code == 200
