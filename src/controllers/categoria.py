from sqlalchemy.orm import Session
from src.models.categoria import Categoria
from src.schemas.categoria import CategoriaCreate

def create_categoria(db: Session, categoria: CategoriaCreate):
    db_categoria = Categoria(**categoria.dict())
    db.add(db_categoria)
    db.commit()
    db.refresh(db_categoria)
    return db_categoria

def get_categoria(db: Session, categoria_id: int):
    return db.query(Categoria).filter(Categoria.id == categoria_id).first()

def get_categorias(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Categoria).offset(skip).limit(limit).all()

def update_categoria(db: Session, categoria_id: int, categoria: CategoriaCreate):
    db_query = db.query(Categoria).filter(Categoria.id == categoria_id)
    db_query.update(categoria.dict())
    db.commit()
    return db_query.first()

def delete_categoria(db: Session, categoria_id: int):
    db_query = db.query(Categoria).filter(Categoria.id == categoria_id)
    db_query.delete()
    db.commit()
    
