from pydantic import BaseModel

class ProdutoBase(BaseModel):
    nome: str
    descricao: str
    preco: float

class ProdutoCreate(ProdutoBase):
    pass

class Produto(ProdutoBase):
    id: int

    class Config:
        orm_mode = True
