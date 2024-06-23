from pydantic import BaseModel

class ProdutoEntrada(BaseModel):
    descricao: str
    valor: float
    quantidade: int
    imagem: str
    categoria_id: int
    
class ProdutoSaida(ProdutoEntrada):
    id: int
    venda: int
    categoria_descricao: str
    dolar: float

class ProdutoCreate(ProdutoEntrada):
    id: int