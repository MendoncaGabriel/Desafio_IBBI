from sqlalchemy.orm import Session
from src.models.produto import Produto
from src.schemas.produto import ProdutoCreate, ProdutoSchema
from src.models.categoria import Categoria

def create(db: Session, produto: ProdutoCreate):
    # Obtém a categoria associada ao produto
    categoria = db.query(Categoria).filter(Categoria.id == produto.categoria_id).first()
    
    # Cria o objeto Produto no banco de dados
    db_produto = Produto(**produto.dict(), categoria=categoria)
    db.add(db_produto)
    db.commit()
    db.refresh(db_produto)

    # Retorna o produto com a descrição da categoria
    return ProdutoSchema(
        id=db_produto.id,
        descricao=db_produto.descricao,
        valor=db_produto.valor,
        quantidade=db_produto.quantidade,
        categoria_id=db_produto.categoria_id,
        categoria_descricao=categoria.descricao
    )


def getById(db: Session, id: int):
    produto = db.query(Produto).join(Categoria, Produto.categoria_id == Categoria.id).filter(Produto.id == id).first()
    
    if produto:
        data = ProdutoSchema(
            id = produto.id,
            descricao = produto.descricao,
            valor = produto.valor,
            quantidade = produto.quantidade,
            categoria_id = produto.categoria_id,
            categoria_descricao = produto.categoria.descricao 
        )
        return data
    return None

def getByOffset(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Produto).offset(skip).limit(limit).all()

def update(db: Session, id: int, produto: ProdutoCreate):
    db_query = db.query(Produto).filter(Produto.id == id)
    db_query.update(produto.dict())
    db.commit()
    return db_query.first()

def delete(db: Session, id: int):
    db_query = db.query(Produto).filter(Produto.id == id)
    db_query.delete()
    db.commit()
