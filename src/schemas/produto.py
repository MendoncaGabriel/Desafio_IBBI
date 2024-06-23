from pydantic import BaseModel

class ProdutoEntrada(BaseModel):
    descricao: str
    valor: float
    quantidade: int
    imagem: str
    categoria_id: int
    
class ProdutoSaida(BaseModel):
    id: int
    descricao: str
    valor: float
    quantidade: int
    categoria_id: int
    imagem: str
    categoria_descricao: str
    dolar: float
