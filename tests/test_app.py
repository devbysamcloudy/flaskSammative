import pytest
from app import app, db

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_add_item(client):
    response = client.post('/items', json={
        "name": "Test",
        "quantity": 1,
        "price": 10
    })
    assert response.status_code == 201

def test_get_items(client):
    response = client.get('/items')
    assert response.status_code == 200

def test_delete_item(client):
    client.post('/items', json={"name": "Test", "quantity": 1, "price": 10})
    response = client.delete('/items/1')
    assert response.status_code == 200