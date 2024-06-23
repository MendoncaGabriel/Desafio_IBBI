from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from src.controllers.categoria import create, getByOffset, getById, update, delete
from src.schemas.categoria import CategoriaEntrada, CategoriaSaida
from src.utilities.auth import checkAuthorization
from config.database import get_db

router = APIRouter()

@router.post("/", response_model=CategoriaEntrada)
def criar_categoria(
    produto: CategoriaEntrada,
    db: Session = Depends(get_db),
    access: dict = Depends(checkAuthorization)
):
    return create(db, produto)

@router.get("/", response_model=List[CategoriaSaida])
def listar_categorias(
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(get_db)
):
    return getByOffset(db, skip=skip, limit=limit)

@router.get("/{id}", response_model=CategoriaSaida)
def obter_categoria_por_id(
    id: int,
    db: Session = Depends(get_db)
):
    categoria = getById(id)
    if categoria is None:
        raise HTTPException(status_code=404, detail="Categoria não encontrada")
    return categoria

@router.put("/{id}", response_model=CategoriaSaida)
def atualizar_categoria(
    id: int,
    categoria: CategoriaEntrada,
    db: Session = Depends(get_db),
    access: dict = Depends(checkAuthorization)
):
    categoria_atualizada = update(id, categoria)
    if categoria_atualizada is None:
        raise HTTPException(status_code=404, detail="Categoria não encontrada")
    return categoria_atualizada

@router.delete("/{id}", response_model=CategoriaSaida)
def deletar_categoria(
    id: int,
    db: Session = Depends(get_db),
    access: dict = Depends(checkAuthorization)
):
    categoria_deletada = delete(id)
    if categoria_deletada is None:
        raise HTTPException(status_code=404, detail="Categoria não encontrada")
    return categoria_deletada
