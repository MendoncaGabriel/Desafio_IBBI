from sqlalchemy.orm import Session
from src.models.produto import Produto
from src.schemas.produto import ProdutoCreate

def create_produto(db: Session, produto: ProdutoCreate):
    db_produto = Produto(**produto.dict())
    db.add(db_produto)
    db.commit()
    db.refresh(db_produto)
    return db_produto

def get_produto(db: Session, produto_id: int):
    return db.query(Produto).filter(Produto.id == produto_id).first()

def get_produtos(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Produto).offset(skip).limit(limit).all()

def update_produto(db: Session, produto_id: int, produto: ProdutoCreate):
    db_query = db.query(Produto).filter(Produto.id == produto_id)
    db_query.update(produto.dict())
    db.commit()
    return db_query.first()

def delete_produto(db: Session, produto_id: int):
    db_query = db.query(Produto).filter(Produto.id == produto_id)
    db_query.delete()
    db.commit()
