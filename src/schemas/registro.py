from pydantic import BaseModel

class RegistroEntrada(BaseModel):
    observacao: str
    nome_cliente: str
    produto_id: int
    quantidade: int
    usuario_id: int
    data: str
    
class RegistroSaida(RegistroEntrada):
    id: int

    class Config:
        orm_mode = True
