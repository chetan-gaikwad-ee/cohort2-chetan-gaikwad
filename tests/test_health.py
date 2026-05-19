from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health_returns_ok():
    response = client.get("/health")
    assert response.status_code == 200

    data = response.json()
    assert data["status"] == "ok"
    assert "timestamp" in data
    assert data["version"] == "0.1.0"
    assert data["environment"] == "development"


def test_unknown_route_returns_404():
    response = client.get("/nonexistent")
    assert response.status_code == 404


def test_health_rejects_post():
    response = client.post("/health")
    assert response.status_code == 405
