import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "scripts")))

from fastapi.testclient import TestClient
from scripts.main import app
from scripts.dependencies import app_secret
from scripts.jwt_utils import create_jwt_token
import datetime


client = TestClient(app)

app_data = {"app_name": "food_frost_test_app"}
token_expiration = datetime.timedelta(days=30)
jwt_token = create_jwt_token(app_data, app_secret, token_expiration)


def test_log_event():
    event_type = "test_event"
    event_data = {"key": "value"}

    response = client.post(
        "/events",
        json={"event_type": event_type, "event_data": event_data},
        headers={"Authorization": f"Bearer {jwt_token}"}
    )

    assert response.status_code == 200
    assert "event_id" in response.json()


def test_log_event_missing_data():
    response = client.post(
        "/events",
        json={"event_data": {"key": "value"}},
        headers={"Authorization": f"Bearer {jwt_token}"}
    )

    assert response.status_code == 422


def test_log_event_invalid_token():
    response = client.post(
        "/events",
        json={"event_type": "test_event", "event_data": {"key": "value"}},
        headers={"Authorization": "Bearer invalid_token"}
    )

    assert response.status_code == 401
