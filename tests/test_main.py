from app.main import app
from fastapi.testclient import TestClient

client = TestClient(app)

def test_convert_btc_to_usd():
    response = client.get("/convert?btc=1&currency=usd")
    assert response.status_code == 200
    data = response.json()
    assert "converted_value" in data
    assert data["btc"] == 1
    assert data["currency"] == "usd"

def test_invalid_currency():
    response = client.get("/convert?btc=1&currency=abc")
    assert response.status_code == 500
