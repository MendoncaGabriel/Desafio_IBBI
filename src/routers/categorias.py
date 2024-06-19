from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.config.database import SessionLocal
import src.controllers.categoria as categoria_controller
from src.schemas.categoria import CategoriaCreate, CategoriaSchema

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model = CategoriaSchema)
def create (produto: CategoriaCreate, db: Session = Depends(get_db)):
    return categoria_controller.create(db, produto)
    
@router.get("/{id}", response_model = CategoriaSchema)
def getById (id: int, db: Session = Depends(get_db)):
    data = categoria_controller.getById(db, id)
    if data is None:
        raise HTTPException(status_code=404, detail="Categoria não encontrada")
    return data

@router.get("/", response_model=list[CategoriaSchema])
def getByOffset(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    data = categoria_controller.getByOffset(db, skip=skip, limit=limit)
    return data

@router.put("/{id}", response_model = CategoriaSchema)
def update(
    id: int, categoria: CategoriaCreate, db: Session = Depends(get_db)
):
    data = categoria_controller.update(db, id, categoria)
    if data is None:
        raise HTTPException(status_code=404, detail="Categoria não encontrada")
    return data

@router.delete("/{id}", response_model=CategoriaSchema)
def delete(id: int, db: Session = Depends(get_db)):
    data = categoria_controller.delete(db, id)
    if data is None:
        raise HTTPException(status_code=404, detail="Categoria não encontrada")
    return data