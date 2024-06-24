from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from src.controllers import categoria as Controller
from src.schemas.categoria import CategoriaEntrada, CategoriaSaida
from src.utilities.auth import checkAuthorization
from config.database import get_db

router = APIRouter()

@router.post("/", response_model=CategoriaSaida)
def create(
    categoria_data: CategoriaEntrada,
    db: Session = Depends(get_db),
    # access: dict = Depends(checkAuthorization)
):
    return Controller.create(db, categoria_data)

@router.get("/", response_model=List[CategoriaSaida])
def get_by_offset(
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(get_db)
):
    return Controller.get_by_offset(db, skip=skip, limit=limit)

@router.get("/{id}", response_model=CategoriaSaida)
def get_by_id(
    id: int,
    db: Session = Depends(get_db)
):
    return Controller.get_by_id(db, id)

@router.put("/{id}", response_model=CategoriaSaida)
def categoria_update(
    id: int,
    categoria_data: CategoriaEntrada,
    db: Session = Depends(get_db),
    # access: dict = Depends(checkAuthorization)
):
    return Controller.update(db, id, categoria_data)

@router.delete("/{id}", response_model=CategoriaSaida)
def categoria_delete(
    id: int,
    db: Session = Depends(get_db),
    # access: dict = Depends(checkAuthorization)
):
    return Controller.update(db, id)
