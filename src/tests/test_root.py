import pytest
from fastapi.testclient import TestClient
from configtest import client  

def test_get_root(client: TestClient) -> None:
    response = client.get("/")
    body = response.json()
    # Verificar se está vindo status 200
    assert response.status_code == 200
    
    # Verificar propriedade
    assert body["mensagem"] == "api de papeis"
