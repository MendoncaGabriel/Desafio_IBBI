from pydantic import BaseModel

class RegistroEntrada(BaseModel):
    data: str
    hora: str
    descricao_produto: str
    nome_cliente: str
    nome_vendedor: str
    observacao: str
    
class RegistroSaida(RegistroEntrada):
    id: int

    class Config:
        orm_mode = True
