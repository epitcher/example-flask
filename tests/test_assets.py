import json
import pytest
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    with app.test_client() as client:
        yield client

def test_items(client):
    response = client.get('/assets')
    assert response.status_code == 200
    assert b'Assets' in response.data

def test_item(client):
    response = client.get('/asset/2')
    assert response.status_code == 200
    assert b'Asset' in response.data
    
def test_item_not_found(client):
    response = client.get('/asset/99')
    assert response.status_code == 404
    assert response.data == b'Asset not found'
