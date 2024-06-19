from sqlalchemy.orm import Session
from src.models.produto import Produto
from src.models.categoria import Categoria
from sqlalchemy.orm import joinedload
from src.schemas.produto import ProdutoCreate, Produto as ProdutoSchema

def create_produto(db: Session, produto: ProdutoCreate):
    db_produto = Produto(**produto.dict())
    db.add(db_produto)
    db.commit()
    db.refresh(db_produto)
    return db_produto

def getById_produto(db: Session, produto_id: int):
    produto = db.query(Produto).\
        join(Categoria, Produto.categoria_id == Categoria.id).\
        filter(Produto.id == produto_id).\
        first()

    if produto:
        # Crie um objeto ProdutoSchema com a descrição da categoria
        produto_dict = ProdutoSchema(
            id=produto.id,
            descricao=produto.descricao,
            valor=produto.valor,
            quantidade=produto.quantidade,
            categoria_id=produto.categoria_id,
            categoria_descricao=produto.categoria.descricao  # Acessando a descrição da categoria
        )
        return produto_dict

    return None

def getByOffset_produto(db: Session, skip: int = 0, limit: int = 10):
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
