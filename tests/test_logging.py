import logging

from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_request_log_is_emitted(caplog):
    with caplog.at_level(logging.INFO, logger="app.request"):
        response = client.get("/health")
        assert response.status_code == 200

    request_logs = [r for r in caplog.records if r.message == "Request completed"]
    assert len(request_logs) >= 1

    record = request_logs[-1]
    assert record.method == "GET"
    assert record.path == "/health"
    assert record.status_code == 200
    assert hasattr(record, "duration_ms")
