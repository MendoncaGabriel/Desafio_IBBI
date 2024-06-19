from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.config.database import SessionLocal, engine
from src.controllers.categoria import (
    create_categoria,
    get_categoria,
    get_categorias,
    update_categoria,
    delete_categoria    
)

from src.schemas.categoria import CategoriaCreate, Categoria

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
@router.post("/", response_model = Categoria)
def create_new_categoria(categoria: CategoriaCreate, db: Session = Depends(get_db)):
    return create_categoria(db, categoria)
    
@router.get("/{categoria_id}", response_model=Categoria)
def read_categoria(categoria_id: int, db: Session = Depends(get_db)):
    db_categoria =  get_categoria(db, categoria_id)
    if db_categoria is None:
        raise HTTPException(status_code=404, detail="Categoria não encontrada")
    return db_categoria

@router.get("/", response_model=list[Categoria])
def read_categoria(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    categorias = get_categorias(db, skip=skip, limit=limit)
    return categorias

@router.put("/{categoria_id}", response_model=Categoria)
def update_existing_categoria(
    categoria_id: int, categoria: CategoriaCreate, db: Session = Depends(get_db)
):
    db_categoria = update_categoria(db, categoria_id, categoria)
    if db_categoria is None:
        raise HTTPException(status_code=404, detail="Categoria não encontrada")
    return db_categoria

@router.delete("/{categoria_id}", response_model=Categoria)
def delete_existing_categoria(categoria_id: int, db: Session = Depends(get_db)):
    db_categoria = get_categoria(db, categoria_id)
    if db_categoria is None:
        raise HTTPException(status_code=404, detail="Categoria não encontrada")
    delete_categoria(db, categoria_id)
    return db_categoria
    

