from sqlalchemy.orm import Session
from src.models.categoria import Categoria
from src.schemas.categoria import CategoriaBase, CategoriaSchema

def create(db: Session, categoria_data: CategoriaBase):
    # Criar uma nova categoria no banco de dados
    data = Categoria(**categoria_data.dict())
    db.add(data)
    db.commit()
    db.refresh(data)
    return data

def getById(db: Session, categoria_id: int):
    # Buscar uma categoria pelo seu ID
    return db.query(Categoria).filter(Categoria.id == categoria_id).first()

def getByOffset(db: Session, skip: int = 0, limit: int = 10):
    # Listar categorias com paginação
    return db.query(Categoria).offset(skip).limit(limit).all()

def update(db: Session, categoria_id: int, categoria_data: CategoriaBase):
    # Atualizar uma categoria pelo seu ID
    db_query = db.query(Categoria).filter(Categoria.id == categoria_id)
    db_query.update(categoria_data.dict(exclude_unset=True))  # Update apenas os campos definidos
    db.commit()
    return db_query.first()

def delete(db: Session, categoria_id: int):
    # Deletar uma categoria pelo seu ID
    db_query = db.query(Categoria).filter(Categoria.id == categoria_id)
    db_query.delete()
    db.commit()
