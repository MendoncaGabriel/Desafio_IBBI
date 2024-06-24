from sqlalchemy.orm import Session
from sqlalchemy import desc
from src.models.produto import Produto
from src.models.categoria import Categoria
from src.schemas.produto import ProdutoSaida, ProdutoEntrada
from src.utilities.converter import realDolar, getDolar
from fastapi import HTTPException
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from typing import List

def create(db: Session, produto: ProdutoEntrada):
    try:
        novo_produto = Produto(**produto.model_dump())
        db.add(novo_produto)
        db.commit()
        db.refresh(novo_produto) 
        return novo_produto
    
    except IntegrityError as error:
        db.rollback()
        raise HTTPException(status_code=400, detail="Já existe um produto com esta descrição") from error
    
    except SQLAlchemyError as error:
        db.rollback()
        raise HTTPException(status_code=500, detail="Erro interno do servidor") from error

def get_by_id(db: Session, id: int):
    try:
        produto = (
            db.query(Produto)
            .outerjoin(Produto.categoria)
            .filter(Produto.id == id)
            .first()
        )
        
        if produto is None:
            raise HTTPException(status_code=404, detail=f"Produto com id {id} não encontrado")

        return ProdutoSaida(
            id=produto.id,
            descricao=produto.descricao,
            valor=produto.valor,
            quantidade=produto.quantidade,
            categoria_id=produto.categoria_id,
            imagem=produto.imagem,
            venda=produto.venda,
            categoria_descricao=produto.categoria.descricao if produto.categoria else None,
            dolar=realDolar(produto.valor)
        )
        
    except SQLAlchemyError as error:
        db.rollback()
        raise HTTPException(status_code=500, detail="Erro interno do servidor") from error
    
def get_by_descricao(db: Session, descricao: str):
    try:
        produto = (
            db.query(Produto)
            .outerjoin(Produto.categoria)
            .filter(Produto.descricao == descricao)
            .first()
        )
        
        if produto is None:
            raise HTTPException(status_code=404, detail=f"Produto com descricão {descricao} não encontrado")

        return ProdutoSaida(
            id=produto.id,
            descricao=produto.descricao,
            valor=produto.valor,
            quantidade=produto.quantidade,
            categoria_id=produto.categoria_id,
            imagem=produto.imagem,
            venda=produto.venda,
            categoria_descricao=produto.categoria.descricao if produto.categoria else None,
            dolar=realDolar(produto.valor)
        )
        
    except SQLAlchemyError as error:
        db.rollback()
        raise HTTPException(status_code=500, detail="Erro interno do servidor") from error

def get_by_offset(db: Session, skip: int = 0, limit: int = 10):
    try:
        produtos = db.query(Produto).join(Categoria).offset(skip).limit(limit).all()
        produtos_schema = []
        cotacao = getDolar()
        
        for produto in produtos:
            produto_schema = ProdutoSaida(
                id=produto.id,
                descricao=produto.descricao,
                valor=produto.valor,
                quantidade=produto.quantidade,
                categoria_id=produto.categoria_id,
                imagem=produto.imagem,
                categoria_descricao=produto.categoria.descricao,
                dolar=round(produto.valor / cotacao, 2),
                venda=produto.venda
            )
            produtos_schema.append(produto_schema)
        return produtos_schema
    
    except SQLAlchemyError as error:
        raise HTTPException(status_code=500, detail="Erro interno do servidor") from error

def update(db: Session, id: int, produto: ProdutoEntrada):
    try:
        # Verifica se a descrição já existe em outro produto
        descricao_existente = db.query(Produto).filter(Produto.descricao == produto.descricao, Produto.id != id).first()
        if descricao_existente:
            raise HTTPException(status_code=400, detail="Já existe um produto com esta descrição")

        # Atualizar o produto pelo ID
        produto_update = db.query(Produto).filter(Produto.id == id)
        produto_update.update(produto.model_dump(exclude_unset=True))
        db.commit()
        
        return produto_update.first()
    except SQLAlchemyError as error:
        db.rollback()
        raise HTTPException(status_code=500, detail="Erro interno do servidor ao atualizar o produto") from error

def delete(db: Session, id: int):
    try:
        produto = db.query(Produto).filter(Produto.id == id).first()
        if not produto:
            raise HTTPException(status_code=404, detail=f"Produto com ID {id} não encontrado")

        db.delete(produto)
        db.commit()

        return produto
    
    except SQLAlchemyError as error:
        db.rollback()
        print(error)
        raise HTTPException(status_code=500, detail="Erro interno do servidor") from error

def get_by_categoria(db: Session, categorias: List[str]):
    try:
        produtos = db.query(Produto).join(Categoria).filter(Categoria.descricao.in_(categorias)).all()
        produtos_schema = []
        cotacao = getDolar() 

        for produto in produtos:
            produto_schema = ProdutoSaida(
                id=produto.id,
                valor=produto.valor,
                categoria_descricao=produto.categoria.descricao if produto.categoria else None,
                descricao=produto.descricao,
                quantidade=produto.quantidade,
                categoria_id=produto.categoria_id,
                imagem=produto.imagem,
                venda=produto.venda,
                dolar=round(produto.valor / cotacao, 2)
            )
            produtos_schema.append(produto_schema)
        
        return produtos_schema
        
    except SQLAlchemyError as error:
        raise HTTPException(status_code=500, detail="Erro interno do servidor") from error

def mais_vendidos(db: Session, limit: int = 10):
   try:
        produtos = db.query(Produto).join(Categoria).order_by(desc(Produto.venda)).limit(limit).all()
        produtos_schema = []
        cotacao = getDolar()
        
        for produto in produtos:
            produto_schema = ProdutoSaida(
                id=produto.id,
                descricao=produto.descricao,
                valor=produto.valor,
                quantidade=produto.quantidade,
                categoria_id=produto.categoria_id,
                imagem=produto.imagem,
                venda=produto.venda,
                categoria_descricao=produto.categoria.descricao if produto.categoria else None,
                dolar=round(produto.valor / cotacao, 2)
            )
            produtos_schema.append(produto_schema)
        return produtos_schema
        
   except SQLAlchemyError as error:
       print(error)
       raise HTTPException(status_code=500, detail="Erro interno do servidor") from error
