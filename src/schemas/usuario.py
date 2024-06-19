from pydantic import BaseModel

class UsuarioBase(BaseModel):
    nome: str
    login: str
    senha: str

class UsuarioCreate(UsuarioBase):
    pass

class ProutoSchema(UsuarioBase):
    id: int

    class Config:
        orm_mode = True