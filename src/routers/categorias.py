from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from src.controllers.categoria import create, get_by_offset, get_by_id, update, delete
from src.schemas.categoria import CategoriaEntrada, CategoriaSaida
from src.utilities.auth import checkAuthorization
from config.database import get_db

router = APIRouter()

@router.post("/", response_model=CategoriaSaida)
def criar_categoria(
    categoria_data: CategoriaEntrada,
    db: Session = Depends(get_db),
    access: dict = Depends(checkAuthorization)
):
    return create(db, categoria_data)

@router.get("/", response_model=List[CategoriaSaida])
def listar_categorias(
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(get_db)
):
    return get_by_offset(db, skip=skip, limit=limit)

@router.get("/{id}", response_model=CategoriaSaida)
def obter_categoria_por_id(
    id: int,
    db: Session = Depends(get_db)
):
    return get_by_id(db, id)

@router.put("/{id}", response_model=CategoriaSaida)
def atualizar_categoria(
    id: int,
    categoria_data: CategoriaEntrada,
    db: Session = Depends(get_db),
    access: dict = Depends(checkAuthorization)
):
    return update(db, id, categoria_data)

@router.delete("/{id}", response_model=CategoriaSaida)
def deletar_categoria(
    id: int,
    db: Session = Depends(get_db),
    access: dict = Depends(checkAuthorization)
):
    return delete(db, id)
