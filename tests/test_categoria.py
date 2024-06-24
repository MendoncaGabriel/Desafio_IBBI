from fastapi.testclient import TestClient
from src.main import app

cliente = TestClient(app)

# Variáveis globais
teste_descricao = "Categoria"
teste_id = None  


def test_get_by_offset_categoria():
    res = cliente.get("/categoria")
    assert res.status_code == 200
    assert isinstance(res.json(), list)
    if len(res.json()) > 0:
        assert all(isinstance(item, dict) and "descricao" in item and "id" in item for item in res.json())

def test_create_categoria():
    global teste_id, teste_descricao
    
    nova_categoria = {"descricao": teste_descricao}
    res = cliente.post("/categoria", json=nova_categoria)
    
    assert res.status_code == 200, f"Erro ao criar categoria: {res.json()}"
    data = res.json()
    assert data["descricao"] == nova_categoria["descricao"]
    assert "id" in data
    teste_id = data["id"]  

def test_get_by_id_categoria():
    global teste_id
        
    res = cliente.get(f"/categoria/{teste_id}")
    
    if res.status_code == 200:
        assert isinstance(res.json(), dict)
        assert "descricao" in res.json()
        assert "id" in res.json()
    elif res.status_code == 404:
        assert False, f"Categoria com ID {teste_id} não encontrada."
    else:
        assert False, f"Erro inesperado ao buscar categoria por ID {teste_id}: {res.status_code}"

def test_update_categoria():
    global teste_id
        
    atualizacao_categoria = {"descricao": "Categoria Atualizada"}
    res_update = cliente.put(f"/categoria/{teste_id}", json=atualizacao_categoria)
    
    assert res_update.status_code == 200, f"Erro ao atualizar categoria: {res_update.json()}"
    data_update = res_update.json()
    assert data_update["descricao"] == atualizacao_categoria["descricao"]
    assert data_update["id"] == teste_id

def test_delete_categoria():
    global teste_id
    
    res = cliente.delete(f"/categoria/{teste_id}")
    
    if res.status_code == 200:
        res_get = cliente.get(f"/categoria/{teste_id}")
        assert res_get.status_code == 404, f"A categoria com id: {teste_id} ainda esta sendo recuperada apois a exclusão"
    elif res.status_code == 404:
        pass
    else:
        assert False, f"Erro inesperado ao deletar categoria com id {teste_id}, status: {res.status_code} "