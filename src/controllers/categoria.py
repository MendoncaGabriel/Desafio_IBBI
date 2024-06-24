from sqlalchemy.orm import Session
from src.models.categoria import Categoria
from src.schemas.categoria import CategoriaEntrada, CategoriaSaida
from fastapi import HTTPException
from sqlalchemy.exc import SQLAlchemyError
from typing import List

# FUNÇÕES AUXILIARES
def check_categoria_by_id(db: Session, id: int) -> Categoria:
    return db.query(Categoria).filter(Categoria.id == id).first()

def check_categoria_by_descricao(db: Session, categoria: CategoriaEntrada) -> Categoria:
    return db.query(Categoria).filter(Categoria.descricao == categoria.descricao).first()

def check_categoria_existing_by_id_and_descricao(db: Session, categoria: CategoriaEntrada, id: int) -> Categoria:
    return db.query(Categoria).filter(
        Categoria.descricao == categoria.descricao,
        Categoria.id != id
    ).first()

# CONTROLLERS
def create(db: Session, categoria: CategoriaEntrada) -> CategoriaSaida:
    try:
        # Verificar categoria com mesma descrição já existe
        check_categ = check_categoria_by_descricao(db, categoria)
        if check_categ:
            raise HTTPException(
                status_code=400, 
                detail=f"Categoria com a descrição: {categoria.descricao}, id: {check_categ.id} já existe"
            )

        categoria_create = Categoria(**categoria.model_dump())
        db.add(categoria_create)
        db.commit()
        db.refresh(categoria_create)
        return categoria_create
    
    except SQLAlchemyError as error:
        db.rollback()
        raise HTTPException(status_code=500, detail="Erro interno do servidor: categoria -> create") from error

def get_by_id(db: Session, id: int) -> CategoriaSaida:
    try:
        categoria = db.query(Categoria).filter(Categoria.id == id).first()
        
        if not categoria:
            raise HTTPException(status_code=404, detail=f"Categoria com o id: {id} não encontrada")
        
        return categoria

    except SQLAlchemyError as error:
        raise HTTPException(status_code=500, detail="Erro interno do servidor: categoria -> get_by_id") from error

def get_by_offset(db: Session, skip: int = 0, limit: int = 10) -> List[CategoriaSaida]:
    try:
        categorias = db.query(Categoria).offset(skip).limit(limit).all()
        
        if len(categorias) == 0:
            raise HTTPException(status_code=404, detail=f"Nenhum produto encontrado no offset: {skip}, limit: {limit}")
        
        return categorias
    
    except SQLAlchemyError as error:
        raise HTTPException(status_code=500, detail="Erro interno do servidor: categoria -> get_by_offset") from error

def update(db: Session, id: int, categoria: CategoriaEntrada) -> CategoriaSaida:
    try:
        # Verifica se a descrição ja existe em outra categoria
        descricao_existente = check_categoria_existing_by_id_and_descricao(db, categoria, id)
        if descricao_existente:
            raise HTTPException(status_code=400, detail=f"Já existe uma categoria com esta descrição: {descricao_existente.descricao}")
        
        categoria_update = db.query(Categoria).filter(Categoria.id == id)
        
        if not categoria_update.first():
            raise HTTPException(status_code=404, detail=f"Categoria com o id: {id}, não encontrada para atualização")
        
        categoria_update.update(categoria.model_dump(exclude_unset=True))
        db.commit()
        
        return categoria_update.first()
    except SQLAlchemyError as error:
        db.rollback()
        raise HTTPException(status_code=500, detail="Erro interno do servidor: categoria -> update") from error

def delete(db: Session, id: int):
    try:
        categoria = check_categoria_by_id(db, id)
        
        if not categoria:
            raise HTTPException(status_code=404, detail=f"Categoria com id: {id}, não encontrado para remoção")
        
        db.delete(categoria)
        db.commit()
        return categoria
    except SQLAlchemyError as error:
        db.rollback()
        raise HTTPException(status_code=500, detail="Erro interno do servidor: categoria -> delete") from error
