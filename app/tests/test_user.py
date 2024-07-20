import pytest
from fastapi.testclient import TestClient

from app import create_app

client = TestClient(create_app(), "http://127.0.0.1:8000")


class TestUser:

    def test_regist(self) -> None:
        data = {
            "email": "test@test.com",
            "password": "1aA@3456",
            "user_name": "Fighters",
            "verify_code": "123456",
        }
        response = client.post(
            "regist",
            json=data,
        )
        print(response.content)
        assert response.status_code == 200

    def test_login(self) -> None:
        data = {"email": "test@test.com", "password": "1aA@3456"}
        response = client.post(
            "login",
            json=data,
        )
        print(response.content)
        assert response.status_code == 200


if __name__ == "__main__":
    pytest.main(["-vs"])
