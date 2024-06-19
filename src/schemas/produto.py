from pydantic import BaseModel

class ProdutoBase(BaseModel):
    descricao: str
    valor: float
    quantidade: int

class ProdutoCreate(ProdutoBase):
    categoria_id: int

class ProdutoSchema(ProdutoBase):
    id: int
    categoria_id: int
    categoria_descricao: str  

    class Config:
        orm_mode = True
