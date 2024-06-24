from fastapi.testclient import TestClient
from src.main import app
from datetime import datetime

cliente = TestClient(app)
registro_id = None
produto_id = None
categoria_id = None

def test_create_registro():
    global registro_id, produto_id, categoria_id
    
    # criar categoria
    nova_categoria = {"descricao": f"Descrição {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"}
    res_categ = cliente.post("/categoria", json=nova_categoria)
    assert res_categ.status_code == 200, f"Erro ao criar categoria: {res_categ.json()}"
    data_categ = res_categ.json()
    
    categoria_id = data_categ["id"]
    
    # criar produto
    novo_produto = {
        "descricao": f"Produto de teste {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        "valor": 999,
        "quantidade": 1,
        "imagem": "string",
        "categoria_id": data_categ["id"]
    }
    res_prod = cliente.post("/produto", json=novo_produto)
    assert res_prod.status_code == 200, f"Erro ao criar produto: {res_prod.json()}"
    data_prod = res_prod.json()
    
    produto_id = data_prod["id"]
    
    # criar registro
    novo_registro = {
        "produto_id": data_prod["id"],
        "nome_cliente": "Pedro",
        "nome_vendedor": "Gabriel",
        "observacao": "teste de registro",
        "quantidade": 1
    }
    
    res_reg = cliente.post("/registro", json=novo_registro)
    assert res_reg.status_code == 200, f"Erro ao criar registro: {res_reg.json()}"
    data_reg = res_reg.json()
    
    registro_id = data_reg["id"]
    
    assert isinstance(data_reg, dict)
    assert "id" in data_reg
    assert "data" in data_reg
    assert "hora" in data_reg
    assert "descricao_produto" in data_reg
    assert data_reg["produto_id"] == data_prod["id"]
    assert "nome_cliente" in data_reg
    assert "nome_vendedor" in data_reg
    assert "observacao" in data_reg
    assert "quantidade" in data_reg

def test_get_by_id_registro():
    global registro_id
    
    res = cliente.get(f"/registro/{registro_id}")
    assert res.status_code == 200
    
    data = res.json()
    assert isinstance(data, dict)
    assert data["id"] == registro_id
    assert "produto_id" in data
    assert "nome_cliente" in data
    assert "nome_vendedor" in data
    assert "observacao" in data
    assert "quantidade" in data
    assert "data" in data
    assert "hora" in data
    assert "descricao_produto" in data
 
def test_delete_registro():
    global registro_id, produto_id, categoria_id
    
    res = cliente.delete(f"/registro/{registro_id}")
    assert res.status_code == 200, f"Erro ao remover registro: {res.json()}"
    
    delete_produto = cliente.delete(f"/produto/{produto_id}")
    assert delete_produto.status_code == 200, f"Erro ao remover produto: {delete_produto.json()}"
    
    delete_categoria = cliente.delete(f"/categoria/{categoria_id}")
    assert delete_categoria.status_code == 200, f"Erro ao remover categoria: {delete_categoria.json()}"