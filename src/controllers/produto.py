from sqlalchemy.orm import Session
from src.models.produto import Produto
from src.schemas.produto import ProdutoBase, ProdutoSchema
from src.models.categoria import Categoria
from src.utilities.converter import realDolar
from fastapi import Query

def create(db: Session, produto: ProdutoBase):
    novo_produto = Produto(**produto.dict())
    db.add(novo_produto)
    db.commit()
    db.refresh(novo_produto)

    return ProdutoBase(
        descricao=novo_produto.descricao,
        valor=novo_produto.valor,
        quantidade=novo_produto.quantidade,
        imagem=novo_produto.imagem,
        categoria_id=novo_produto.categoria_id
    )
        
def getById(db: Session, id: int):
    produto = db.query(Produto).join(Categoria).filter(Produto.id == id).first()
    if produto:
        dolar = realDolar(produto.valor)
        data = ProdutoSchema(
            id=produto.id,
            descricao=produto.descricao,
            valor=produto.valor,
            quantidade=produto.quantidade,
            categoria_id=produto.categoria_id,
            imagem=produto.imagem,
            categoria_descricao=produto.categoria.descricao if produto.categoria else None,
            dolar=dolar
        )
        return data
    return None

def getByOffset(db: Session, skip: int = 0, limit: int = 10):
    produtos = db.query(Produto).join(Categoria).offset(skip).limit(limit).all()
    produtos_schema = []

    for produto in produtos:
        dolar = realDolar(produto.valor)
        produto_schema = ProdutoSchema(
            id=produto.id,
            descricao=produto.descricao,
            valor=produto.valor,
            quantidade=produto.quantidade,
            categoria_id=produto.categoria_id,
            imagem=produto.imagem,
            categoria_descricao=produto.categoria.descricao,
            dolar=dolar
        )
        produtos_schema.append(produto_schema)

    return produtos_schema

def update(db: Session, id: int, produto: ProdutoBase):
    data = db.query(Produto).filter(Produto.id == id)
    data.update(produto.dict())
    db.commit()
    return data.first()

def delete(db: Session, id: int):
    # Verifique se o produto existe
    db_query = db.query(Produto).filter(Produto.id == id)
    produto = db_query.first()
    if produto is None:
        return None

    # Apague o produto
    db_query.delete()
    db.commit()
    return {"msg": "Produto apagado com sucesso!", "produto": produto}

def getByCategoria(db: Session, categorias: list):
    data = []

    for categoria in categorias:
        # Consulta para buscar produtos pela descrição da categoria
        produtos = db.query(Produto).join(Categoria).filter(Categoria.descricao == categoria).all()

        for produto in produtos:
            dolar = realDolar(produto.valor)  # Supondo que realDolar seja uma função válida
            item = ProdutoSchema(
                id=produto.id,
                descricao=produto.descricao,
                valor=produto.valor,
                quantidade=produto.quantidade,
                categoria_id=produto.categoria_id,
                imagem=produto.imagem,
                categoria_descricao=produto.categoria.descricao if produto.categoria else None,
                dolar=dolar
            )
            data.append(item)

    return data

def mais_vendidos(db: Session, limit: int = 10):
    produtos = db.query(Produto).join(Categoria).order_by(Produto.venda.desc()).limit(limit).all()

    return produtos