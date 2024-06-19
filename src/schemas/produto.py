from pydantic import BaseModel

class ProdutoBase(BaseModel):
    descricao: str
    valor: float
    quantidade: int
    categoria_descricao: str

class ProdutoCreate(ProdutoBase):
    categoria_id: int

class Produto(ProdutoBase):
    id: int
    categoria_id: int  # Inclui o campo categoria_id no modelo

    class Config:
        orm_mode = True
