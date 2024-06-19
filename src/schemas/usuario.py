from pydantic import BaseModel

class UsuarioBase(BaseModel):
    login: str
    senha: str

class UsuarioCreate(UsuarioBase):
    nome: str

class UsuarioSchema(UsuarioBase):
    id: int
    nome: str

    class Config:
        orm_mode = True
