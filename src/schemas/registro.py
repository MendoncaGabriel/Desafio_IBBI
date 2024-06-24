from pydantic import BaseModel

class RegistroEntrada(BaseModel):
    produto_id: int
    nome_cliente: str
    nome_vendedor: str
    observacao: str
    quantidade: int
    
class RegistroSaida(RegistroEntrada):
    id: int
    data: str
    hora: str
    valor: float
    total: float
    descricao_produto: str


