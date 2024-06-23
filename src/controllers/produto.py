from sqlalchemy.orm import Session
from sqlalchemy import desc
from src.models.produto import Produto
from src.models.categoria import Categoria
from src.schemas.produto import ProdutoSaida, ProdutoEntrada
from src.utilities.converter import realDolar
from fastapi import HTTPException
from sqlalchemy.exc import SQLAlchemyError
from typing import List

def create(db: Session, produto: ProdutoEntrada) -> Produto:
    try:
        novo_produto = Produto(**produto.model_dump())
        db.add(novo_produto)
        db.commit()
        return novo_produto
    except SQLAlchemyError as error:
        db.rollback()
        raise HTTPException(status_code=500, detail="Erro interno do servidor") from error

def get_by_id(db: Session, id: int) -> ProdutoSaida:
    try:
        produto = (
            db.query(Produto)
            .outerjoin(Produto.categoria)
            .filter(Produto.id == id)
            .first()
        )

        if not produto:
            return None

        return ProdutoSaida(
            id=produto.id,
            descricao=produto.descricao,
            valor=produto.valor,
            quantidade=produto.quantidade,
            categoria_id=produto.categoria_id,
            imagem=produto.imagem,
            categoria_descricao=produto.categoria.descricao if produto.categoria else None,
            dolar=realDolar(produto.valor)
        )
    except SQLAlchemyError as error:
        raise HTTPException(status_code=500, detail="Erro interno do servidor") from error

def get_by_offset(db: Session, skip: int = 0, limit: int = 10) -> List[ProdutoSaida]:
    try:
        produtos = db.query(Produto).join(Categoria).offset(skip).limit(limit).all()
        produtos_schema = []

        for produto in produtos:
            dolar = realDolar(produto.valor)
            produto_schema = ProdutoSaida(
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
    except SQLAlchemyError as error:
        raise HTTPException(status_code=500, detail="Erro interno do servidor") from error

def update(db: Session, id: int, produto: ProdutoSaida) -> ProdutoSaida:
    try:
        db.query(Produto).filter(Produto.id == id).update(produto.model_dump())
        db.commit()
        return produto
    except SQLAlchemyError as error:
        db.rollback()
        raise HTTPException(status_code=500, detail="Erro interno do servidor") from error

def delete(db: Session, id: int) -> ProdutoSaida:
    try:
        produto = db.query(Produto).filter(Produto.id == id).first()
        if not produto:
            raise HTTPException(status_code=404, detail=f"Produto com ID {id} não encontrado")

        db.delete(produto)
        db.commit()

        return produto
    except SQLAlchemyError as error:
        db.rollback()
        raise HTTPException(status_code=500, detail="Erro interno do servidor") from error

def get_by_categoria(db: Session, categorias: List[str]) -> List[ProdutoSaida]:
    try:
        produtos = (
            db.query(Produto)
            .join(Produto.categoria)
            .filter(Produto.categoria.has(Produto.descricao.in_(categorias)))
            .all()
        )

        produtos_schema = [
            ProdutoSaida(
                id=produto.id,
                descricao=produto.descricao,
                valor=produto.valor,
                quantidade=produto.quantidade,
                categoria_id=produto.categoria_id,
                imagem=produto.imagem,
                categoria_descricao=produto.categoria.descricao if produto.categoria else None,
                dolar=realDolar(produto.valor)
            )
            for produto in produtos
        ]
        return produtos_schema
    except SQLAlchemyError as error:
        raise HTTPException(status_code=500, detail="Erro interno do servidor") from error

def mais_vendidos(db: Session, limit: int = 10) -> List[ProdutoSaida]:
   try:
        produtos = (
            db.query(Produto)
            .outerjoin(Produto.categoria)
            .order_by(desc(Produto.venda))
            .limit(limit)
            .all()
        )

        produtos_schema = [
            ProdutoSaida(
                id=produto.id,
                descricao=produto.descricao,
                valor=produto.valor,
                quantidade=produto.quantidade,
                categoria_id=produto.categoria_id,
                imagem=produto.imagem,
                categoria_descricao=produto.categoria.descricao if produto.categoria else None,
                dolar=realDolar(produto.valor)
            )
            for produto in produtos
        ]
        return produtos_schema
   except SQLAlchemyError as error:
       raise HTTPException(status_code=500, detail="Erro interno do servidor") from error
