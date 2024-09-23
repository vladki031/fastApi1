from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_get_products():
    response = client.get("/api/products/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_register_user():
    response = client.post("/api/auth/register", json={"username": "vlad", "password": "vlad2003"})
    assert response.status_code == 201

def test_login():
    response = client.post("/api/auth/login", json={"username": "vlad", "password": "vlad2003"})
    assert response.status_code == 200
    assert "access_token" in response.json()
