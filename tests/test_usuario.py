from fastapi.testclient import TestClient
from src.main import app
from datetime import datetime
import json


cliente = TestClient(app)
usuario_id = None
senha_usuario = "123"
login_usuario = None


def test_signup_usuario():
    global usuario_id, senha_usuario, login_usuario
    login_usuario = f"login-{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    
    novo_usuario = {
        "nome": f"usuario de teste: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        "login": login_usuario,
        "senha": senha_usuario
    }
    res = cliente.post("/usuario/signup", json=novo_usuario)
    res.status_code == 200
    data = res.json()
    
    usuario_id = data["id"]
    
    assert "id" in data
    assert "token" in data
    
def test_login_usuario():
    global login_usuario, senha_usuario
    
    credenciais = {
        "login": login_usuario,
        "senha": senha_usuario
    }
    res = cliente.post("/usuario/login", json=credenciais)
    assert res.status_code == 200
    data = res.json()
    assert "id" in data
    assert "token" in data
    
def test_delete_usuario():
    global usuario_id, senha_usuario, login_usuario
    
    credenciais = {
        "login": login_usuario,
        "senha": senha_usuario
    }
    res = cliente.request("DELETE", f"/usuario/{usuario_id}", json=credenciais)
    assert res.status_code == 200, f"Erro ao deletar usuário: {res.json()}"
    data = res.json()
    assert "msg" in data