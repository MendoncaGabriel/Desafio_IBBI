from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from src.config.database import SessionLocal
from src.controllers import produto as produto_controller  
from src.schemas.produto import ProdutoBase, ProdutoSchema, ProdutoDelete
from src.utilities.auth import checkAuthorization

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=ProdutoBase)
def create(produto: ProdutoBase, db: Session = Depends(get_db), access: dict = Depends(checkAuthorization)):
    return produto_controller.create(db, produto)

@router.get("/{id}", response_model=ProdutoSchema)
def getById(id: int, db: Session = Depends(get_db)):
    data = produto_controller.getById(db, id)
    if data is None:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    return data

@router.get("/getbycategoria", response_model=list[ProdutoSchema])
def getByCategoria(categorias: list[str] = Query(...), db: Session = Depends(get_db)):
    data = produto_controller.getByCategoria(db, categorias)

    if not data:
        raise HTTPException(status_code=404, detail="Produtos não encontrados")

    return data
@router.get("/", response_model=list[ProdutoSchema])
def getByOffset(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return produto_controller.getByOffset(db, skip=skip, limit=limit)

@router.put("/{id}", response_model=ProdutoBase)
def update(id: int, produto: ProdutoBase, db: Session = Depends(get_db), access: dict = Depends(checkAuthorization)):
    data = produto_controller.update(db, id, produto)
    if data is None:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    return data

@router.delete("/{id}", response_model=ProdutoDelete)
def delete(id: int, db: Session = Depends(get_db), access: dict = Depends(checkAuthorization)):
    data = produto_controller.delete(db, id)
    if data is None:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    return data