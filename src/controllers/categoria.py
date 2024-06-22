from sqlalchemy.orm import Session
from src.models.categoria import Categoria
from src.schemas.categoria import CategoriaBase, CategoriaSchema

def create(db: Session, categoria_data: CategoriaBase):
    data = Categoria(**categoria_data.model_dump())
    db.add(data)
    db.commit()
    db.refresh(data)
    return data

def getById(db: Session, categoria_id: int):
    return db.query(Categoria).filter(Categoria.id == categoria_id).first()

def getByOffset(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Categoria).offset(skip).limit(limit).all()

def update(db: Session, categoria_id: int, categoria_data: CategoriaBase):
    db_query = db.query(Categoria).filter(Categoria.id == categoria_id)
    db_query.update(categoria_data.dict(exclude_unset=True))
    db.commit()
    return db_query.first()

def delete(db: Session, categoria_id: int):
    db_query = db.query(Categoria).filter(Categoria.id == categoria_id)
    db_query.delete()
    db.commit()
