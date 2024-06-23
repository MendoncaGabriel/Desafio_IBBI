from pydantic import BaseModel

class RegistroBase(BaseModel):
    observacao: str
    nome_cliente: str
    produto_id: int
    quantidade: int
    usuario_id: int
    data: str
    
class RegistroSchema(RegistroBase):
    id: int

    class Config:
        orm_mode = True
