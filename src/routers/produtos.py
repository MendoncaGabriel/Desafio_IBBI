from fastapi import APIRouter, Depends, HTTPException, Query
from src.controllers import produto as produto_controller  
from src.schemas.produto import ProdutoEntrada, ProdutoSaida
from src.utilities.auth import checkAuthorization
from typing import List, Optional

router = APIRouter()

@router.post("/")
def create(produto: ProdutoEntrada):
    return produto_controller.create(produto)

@router.get("/getbycategoria")
def get_by_categoria(categoria: Optional[List[str]] = Query(None)):
    if categoria is None:
        categoria = []
        
    data = produto_controller.getByCategoria(db, categoria)
    return data

@router.get("/mais_vendidos")
def mais_vendidos():
    return produto_controller.mais_vendidos()
   
@router.get("/")
def getByOffset(skip: int = 0, limit: int = 10):
    return produto_controller.getByOffset(db, skip=skip, limit=limit)

@router.get("/{id}")
def getById(id: int):
    produto = produto_controller.getById(db, id)
    if produto is None:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    return produto

@router.put("/{id}")
def update(id: int, produto: ProdutoSaida, access: dict = Depends(checkAuthorization)):
    produtoUpdate = produto_controller.update(id, produto)
    if produtoUpdate is None:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    return produtoUpdate

@router.delete("/{id}")
def delete(id: int, access: dict = Depends(checkAuthorization)):
    produtoDelete = produto_controller.delete(id)
    if produtoDelete is None:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    return produtoDelete