"""User Information Unit Test."""
from __future__ import annotations

import json
from typing import Any

from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

with open("app/tests/example_data/user_information_request.json", 'r', encoding='UTF-8') as f:
    user_information_request: dict[str, Any] = json.load(f)


def test_get_all_user_information():
    """Test get all user information success."""
    response = client.get("/api/admin/user")
    assert response.status_code == 200


def test_rest_api_user_information():
    """Test add and get user information success."""
    response = client.post("/api/admin/user", json=user_information_request)
    assert response.status_code == 200

    user_id = response.json()["data"]["userID"]

    response = client.put(f"/api/admin/user/{user_id}", json=user_information_request)
    assert response.status_code == 200

    response = client.get(f"/api/admin/user/{user_id}")
    assert response.status_code == 200

    response = client.delete(f"/api/admin/user/{user_id}")
    assert response.status_code == 200


if __name__ == '__main__':
    test_rest_api_user_information()
