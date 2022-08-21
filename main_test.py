import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_index_route():
    response = client.get('/roleUsers/cc4e39f')
    assert response.status_code == 200

def test_index_204():
    response = client.get('/roleUsers/10des4i')
    assert response.status_code == 204