from sqlalchemy.orm import Session
from src.models.categoria import Categoria
from src.schemas.categoria import CategoriaEntrada
from fastapi import HTTPException
from sqlalchemy.exc import SQLAlchemyError

def create(db: Session, categoria_data: CategoriaEntrada):
    try:
        # Verificar se já existe uma categoria com a mesma descrição
        existing_categoria = db.query(Categoria).filter(Categoria.descricao == categoria_data.descricao).first()
        if existing_categoria:
            raise HTTPException(status_code=400, detail=f"Categoria com a descrição: {categoria_data.descricao}, id: {existing_categoria.id} ja existe.", )


        categoria = Categoria(**categoria_data.model_dump())
        db.add(categoria)
        db.commit()
        db.refresh(categoria)
        return categoria
    except SQLAlchemyError as error:
        db.rollback()
        raise HTTPException(status_code=500, detail="Erro interno do servidor: categoria -> create") from error

def get_by_id(db: Session, categoria_id: int) -> Categoria:
    try:
        categoria =  db.query(Categoria).filter(Categoria.id == categoria_id).first()
        
        if categoria is None:
            raise HTTPException(status_code=404, detail=f"Categoria com o id: {categoria_id} não encontrado")
        
        return categoria

    except SQLAlchemyError as error:
        raise HTTPException(status_code=500, detail="Erro interno do servidor: categoria -> get_by_id") from error

def get_by_offset(db: Session, skip: int = 0, limit: int = 10):
    try:
        categorias = db.query(Categoria).offset(skip).limit(limit).all()
        
        if len(categorias) == 0:
            raise HTTPException(status_code=404, detail=f"Nenhum produto encontrado no offset: {skip}, limit: {limit}")
        
        return categorias
    
    except SQLAlchemyError as error:
        raise HTTPException(status_code=500, detail="Erro interno do servidor: categoria -> get_by_offset") from error

def update(db: Session, categoria_id: int, categoria_data: CategoriaEntrada):
    try:
        # Verifica se a descrição já existe em outra categoria
        descricao_existente = db.query(Categoria).filter(
            Categoria.descricao == categoria_data.descricao,
            Categoria.id != categoria_id
        ).first()
        if descricao_existente:
            raise HTTPException(status_code=400, detail=f"Já existe uma categoria com esta descrição: {descricao_existente.descricao}")
        
        categoria = db.query(Categoria).filter(Categoria.id == categoria_id)
        
        if not categoria:
            raise HTTPException(status_code=404, detail=f"Produto com id: {categoria_id}, não encontrado para atualização")
        
        categoria.update(categoria_data.model_dump(exclude_unset=True))
        db.commit()
        
        return categoria.first()
    except SQLAlchemyError as error:
        db.rollback()
        raise HTTPException(status_code=500, detail="Erro interno do servidor: categoria -> update") from error

def delete(db: Session, categoria_id: int):
    try:
        categoria = db.query(Categoria).filter(Categoria.id == categoria_id).first()
        
        if not categoria:
            raise HTTPException(status_code=404, detail=f"Categoria com id: {categoria_id}, não encontrado para remoção")
        
        db.delete(categoria)
        db.commit()
        return categoria
    except SQLAlchemyError as error:
        db.rollback()
        raise HTTPException(status_code=500, detail="Erro interno do servidor: categoria -> delete") from error
