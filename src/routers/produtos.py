from fastapi import APIRouter, Depends, HTTPException, Query
from src.controllers import produto as Controller  
from src.schemas.produto import ProdutoEntrada, ProdutoSaida, ProdutoCreate
from src.utilities.auth import checkAuthorization
from sqlalchemy.orm import Session
from typing import List, Optional
from config.database import get_db

router = APIRouter()

@router.post("/", response_model=ProdutoCreate)
def create(
    produto: ProdutoEntrada,
    db: Session = Depends(get_db)
):
    return Controller.create(db, produto)

@router.get("/getbycategoria", response_model=List[ProdutoSaida])
def get_by_categoria(
    categoria: Optional[List[str]] = Query(None),
    db: Session = Depends(get_db)
):
    if categoria is None:
        categoria = []
    return Controller.get_by_categoria(db, categoria)

@router.get("/mais_vendidos", response_model=List[ProdutoSaida])
def mais_vendidos(
    db: Session = Depends(get_db)
):
    return Controller.mais_vendidos(db)
   
@router.get("/", response_model=List[ProdutoSaida])
def get_by_offset(
    skip: int = 0, 
    limit: int = 10,
    db: Session = Depends(get_db)
):
    return Controller.get_by_offset(db, skip=skip, limit=limit)

@router.get("/descricao", response_model=ProdutoSaida)
def get_by_descricao(
    descricao: str,
    db: Session = Depends(get_db)
):
    return Controller.get_by_descricao(db, descricao)

@router.get("/{id}", response_model=ProdutoSaida)
def get_by_id(
    id: int,
    db: Session = Depends(get_db)
):
    return Controller.get_by_id(db, id)

@router.put("/{id}", response_model=ProdutoEntrada)
def update(
    id: int, 
    produto: ProdutoEntrada, 
    # access: dict = Depends(checkAuthorization),
    db: Session = Depends(get_db)
):
    return Controller.update(db, id, produto)

@router.delete("/{id}", response_model=ProdutoEntrada)
def delete(
    id: int, 
    # access: dict = Depends(checkAuthorization),
    db: Session = Depends(get_db)
):
    return Controller.delete(db, id)
