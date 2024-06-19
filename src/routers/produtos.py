from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.config.database import SessionLocal, engine
from src.controllers.produto import (
    create_produto,
    get_produto,
    get_produtos,
    update_produto,
    delete_produto,
)
from src.schemas.produto import ProdutoCreate, Produto

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model = Produto)
def create_new_produto(produto: ProdutoCreate, db: Session = Depends(get_db)):
    return create_produto(db, produto)

@router.get("/{produto_id}", response_model=Produto)
def read_produto(produto_id: int, db: Session = Depends(get_db)):
    db_produto = get_produto(db, produto_id)
    if db_produto is None:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    return db_produto

@router.get("/", response_model=list[Produto])
def read_produtos(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    produtos = get_produtos(db, skip=skip, limit=limit)
    return produtos

# aqui
@router.put("/{produto_id}", response_model=Produto)
def update_existing_produto(
    produto_id: int, produto: ProdutoCreate, db: Session = Depends(get_db)
):
    db_produto = update_produto(db, produto_id, produto)
    if db_produto is None:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    return db_produto

@router.delete("/{produto_id}", response_model=Produto)
def delete_existing_produto(produto_id: int, db: Session = Depends(get_db)):
    db_produto = get_produto(db, produto_id)
    if db_produto is None:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    delete_produto(db, produto_id)
    return db_produto
