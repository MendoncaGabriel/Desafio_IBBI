from pydantic import BaseModel

class ProdutoBase(BaseModel):
    descricao: str
    valor: float
    quantidade: int
    categoria_id: int
    imagem: str
    venda: int
    
class ProdutoSchema(ProdutoBase):
    id: int
    categoria_descricao: str
    dolar: float
    
class ProdutoDelete(BaseModel):
    msg: str
    produto: ProdutoBase