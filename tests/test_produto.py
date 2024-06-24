from fastapi.testclient import TestClient
from src.main import app
from datetime import datetime

cliente = TestClient(app)

# Variáveis globais
teste_descricao = f"Produto teste: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
produto_id = None
categoria_id = None

# lembrar de remover produto e categoria do produto

def test_get_by_offset_produto():
    res = cliente.get("/produto")
    assert res.status_code == 200
    
    produtos = res.json()
    assert isinstance(produtos, list)
    
    for produto in produtos:
        assert isinstance(produto, dict)
        assert "descricao" in produto
        assert "valor" in produto
        assert "quantidade" in produto
        assert "imagem" in produto
        assert "categoria_id" in produto
        assert "id" in produto
        assert "id" in produto
        assert "venda" in produto
        assert "categoria_descricao" in produto
        assert "dolar" in produto

def test_create_produto():
    global produto_id, teste_descricao, categoria_id
    
    # Criar uma categoria
    categoria = f"categoria teste: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"

    nova_categoria = {"descricao": categoria}
    res_categ = cliente.post("/categoria", json=nova_categoria)
    data_categ = res_categ.json()
    categoria_id = data_categ["id"]
    
    assert res_categ.status_code == 200, f"Erro ao criar categoria no teste create de produto: {res_categ.json()}"
    
    # Criar produto
    novo_produto = {
        "descricao": teste_descricao,
        "valor": 999,
        "quantidade": 99,
        "imagem": "string",
        "categoria_id": data_categ["id"]
    }
    
    res_prod = cliente.post("/produto", json=novo_produto)
    assert res_prod.status_code == 200, f"Erro ao criar produto: {res_prod.json()}"
    data_prod = res_prod.json()
    
    assert data_prod["descricao"] == novo_produto["descricao"]
    assert "id" in data_prod
    assert "valor" in data_prod
    assert "quantidade" in data_prod
    assert "imagem" in data_prod
    assert "categoria_id" in data_prod
    assert data_prod["categoria_id"] == data_categ["id"]
    
    produto_id = data_prod["id"]
    
def test_get_by_id_produto():
    global produto_id
    
    res = cliente.get(f"/produto/{produto_id}")
    assert res.status_code == 200
    
    data = res.json()
    assert isinstance(data, dict)
    assert "descricao" in data
    assert "valor" in data
    assert "quantidade" in data
    assert "imagem" in data
    assert "categoria_id" in data
    assert "id" in data
    assert "venda" in data
    assert "categoria_descricao" in data
    assert "dolar" in data

def test_get_by_descricao():
    global produto_id
    
    # pegar produto
    produto = cliente.get(f"/produto/{produto_id}")
    assert produto.status_code == 200
    data = produto.json()
    print(data)

    # buscar por descricão
    res_desc = cliente.get(f"/produto?categoria={data['categoria_descricao']}")
    assert res_desc.status_code == 200
    data_res_desc = res_desc.json()
    print(data_res_desc)
    
def test_mais_vendidos_produto():
    res = cliente.get("/produto/mais_vendidos")
    assert res.status_code == 200
    data = res.json()
    assert isinstance(data, list)
    
    for produto in data:
        assert isinstance(produto, dict)
        assert "descricao" in produto
        assert "valor" in produto
        assert "quantidade" in produto
        assert "imagem" in produto
        assert "categoria_id" in produto
        assert "id" in produto
        assert "venda" in produto
        assert "categoria_descricao" in produto
        assert "dolar" in produto
    
def test_update_produto():
    global produto_id, categoria_id
    descricao = f"update {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    atualizacao_categoria = {
        "descricao": descricao,
        "valor": 99,
        "quantidade": 50,
        "imagem": "string update",
        "categoria_id": categoria_id
    }
    
    res = cliente.put(f"/produto/{produto_id}", json=atualizacao_categoria)
    res.status_code == 200, f"Erro ao atualizar produto: {res.json()}"
    
    data = res.json()
    assert data["descricao"] == descricao
    
def test_delete():
    global produto_id, categoria_id
    
    res_prod = cliente.delete(f"/produto/{produto_id}")
    assert res_prod.status_code == 200
    
    res_categ = cliente.delete(f"/categoria/{categoria_id}")
    assert res_categ.status_code == 200