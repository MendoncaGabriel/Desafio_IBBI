from pydantic import BaseModel

class ProdutoBase(BaseModel):
    descricao: str
    valor: float
    quantidade: int
    categoria_id: int

class ProdutoSchema(ProdutoBase):
    id: int
    categoria_descricao: str