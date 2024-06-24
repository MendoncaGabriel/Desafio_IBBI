from fastapi.testclient import TestClient   
from src.main import app

cliente = TestClient(app)

def test_read_main_docs():
    res = cliente.get("/docs")
    assert res.status_code == 200