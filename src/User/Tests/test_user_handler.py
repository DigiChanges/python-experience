from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_read_item():
    response = client.get("/api/users")
    assert response.status_code == 200
    assert response.json() == {
        "id": "foo",
        "title": "Foo",
        "description": "There goes my hero",
    }

