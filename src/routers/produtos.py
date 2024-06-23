from fastapi import APIRouter, Depends, HTTPException, Query
from src.controllers import produto as produto_controller  
from src.schemas.produto import ProdutoEntrada, ProdutoSaida
from src.utilities.auth import checkAuthorization
from sqlalchemy.orm import Session
from typing import List, Optional
from config.database import get_db

router = APIRouter()

@router.post("/", response_model=ProdutoSaida)
def create(
    produto: ProdutoEntrada,
    db: Session = Depends(get_db)
):
    return produto_controller.create(db, produto)

@router.get("/getbycategoria", response_model=ProdutoSaida)
def get_by_categoria(
    categoria: Optional[List[str]] = Query(None),
    db: Session = Depends(get_db)
):
    if categoria is None:
        categoria = []
    return produto_controller.get_by_categoria(db, categoria)

@router.get("/mais_vendidos")
def mais_vendidos(
    db: Session = Depends(get_db)
):
    return produto_controller.mais_vendidos(db)
   
@router.get("/", response_model=List[ProdutoSaida])
def get_by_offset(
    skip: int = 0, 
    limit: int = 10,
    db: Session = Depends(get_db)
):
    return produto_controller.get_by_offset(db, skip=skip, limit=limit)

@router.get("/{id}", response_model=ProdutoSaida)
def getById(
    id: int,
    db: Session = Depends(get_db)
):
    produto = produto_controller.get_by_id(db, id)
    if produto is None:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    return produto

@router.put("/{id}", response_model=ProdutoSaida)
def update(
    id: int, 
    produto: ProdutoSaida, 
    access: dict = Depends(checkAuthorization),
    db: Session = Depends(get_db)
):
    produtoUpdate = produto_controller.update(db, id, produto)
    if produtoUpdate is None:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    return produtoUpdate

@router.delete("/{id}", response_model=ProdutoSaida)
def delete(
    id: int, 
    access: dict = Depends(checkAuthorization),
    db: Session = Depends(get_db)
):
    produtoDelete = produto_controller.delete(db, id)
    if produtoDelete is None:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    return produtoDelete