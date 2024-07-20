import json
from fastapi.testclient import TestClient

from app import create_app
import pytest

client = TestClient(create_app(), "http://127.0.0.1:8000")


class TestItem:

    @pytest.fixture
    def login(self):
        data = {"email": "test@test.com", "password": "1aA@3456"}
        response = client.post(
            "login",
            json=data,
        )
        return json.loads(response.content)

    def test_item_list(self, login) -> None:
        token = login["data"]["token"]
        response = client.post(
            "item/list",
            headers={"TOKEN": token},
        )
        print(response.content)
        assert response.status_code == 200


if __name__ == "__main__":
    # client = TestClient(create_app(), "http://127.0.0.1:8000")
    # header = {
    #     "TOKEN": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MjE1MzQwNDYsImlhdCI6MTcyMTQ0NzY0NiwiaXNzIjoicGFwZXJwaWUiLCJkYXRhIjp7InVzZXJfaWQiOjEsImxvZ2luX3RpbWUiOjE3MjE0NDc2NDZ9fQ.6sqQXVSBGn4qHVDQT7ac5IeYPZ-H8L8Xdebfl5nP_ZE"
    # }
    # test_item_list(client, header)
    pytest.main(["-vs"])
