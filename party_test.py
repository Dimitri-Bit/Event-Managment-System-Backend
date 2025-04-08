from main import app
from fastapi.testclient import TestClient

client = TestClient(app)

def test_parties_get_all():
    response = client.get("/party")
    assert response.status_code == 200

def test_parties_get_by_id():
    response = client.get("/party/1")
    assert response.status_code == 200
