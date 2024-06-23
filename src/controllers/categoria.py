from sqlalchemy.orm import Session
from src.models.categoria import Categoria
from src.schemas.categoria import CategoriaEntrada
from fastapi import HTTPException
from sqlalchemy.exc import SQLAlchemyError

def create(db: Session, categoria_data: CategoriaEntrada) -> Categoria:
    try:
        categoria = Categoria(**categoria_data.model_dump())
        db.add(categoria)
        db.commit()
        db.refresh(categoria)
        return categoria
    except SQLAlchemyError as error:
        db.rollback()
        raise HTTPException(status_code=500, detail="Erro interno do servidor") from error

def get_by_id(db: Session, categoria_id: int) -> Categoria:
    try:
        return db.query(Categoria).filter(Categoria.id == categoria_id).first()
    except SQLAlchemyError as error:
        raise HTTPException(status_code=500, detail="Erro interno do servidor") from error

def get_by_offset(db: Session, skip: int = 0, limit: int = 10) -> list:
    try:
        return db.query(Categoria).offset(skip).limit(limit).all()
    except SQLAlchemyError as error:
        raise HTTPException(status_code=500, detail="Erro interno do servidor") from error

def update(db: Session, categoria_id: int, categoria_data: CategoriaEntrada) -> Categoria:
    try:
        db_query = db.query(Categoria).filter(Categoria.id == categoria_id)
        db_query.update(categoria_data.model_dump(exclude_unset=True))
        db.commit()
        return db_query.first()
    except SQLAlchemyError as error:
        db.rollback()
        raise HTTPException(status_code=500, detail="Erro interno do servidor") from error

def delete(db: Session, categoria_id: int) -> Categoria:
    try:
        categoria = db.query(Categoria).filter(Categoria.id == categoria_id).first()
        if categoria:
            db.delete(categoria)
            db.commit()
        return categoria
    except SQLAlchemyError as error:
        db.rollback()
        raise HTTPException(status_code=500, detail="Erro interno do servidor") from error
