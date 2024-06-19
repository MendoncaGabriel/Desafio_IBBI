from sqlalchemy.orm import Session
from src.models.categoria import Categoria
from src.schemas.categoria import CategoriaCreate

def create(db: Session, categoria: CategoriaCreate):
    # .dict() foi mudado para .model_dump()
    data = Categoria(**categoria.model_dump())
    db.add(data)
    db.commit()
    db.refresh(data)
    return data

def getById(db: Session, categoria_id: int):
    return db.query(Categoria).filter(Categoria.id == categoria_id).first()

def getByOffset(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Categoria).offset(skip).limit(limit).all()

def update(db: Session, categoria_id: int, categoria: CategoriaCreate):
    db_query = db.query(Categoria).filter(Categoria.id == categoria_id)
    db_query.update(categoria.dict())
    db.commit()
    return db_query.first()

def delete(db: Session, categoria_id: int):
    db_query = db.query(Categoria).filter(Categoria.id == categoria_id)
    db_query.delete()
    db.commit()
