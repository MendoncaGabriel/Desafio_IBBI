from pydantic import BaseModel

class UsuarioBase(BaseModel):
    nome: str
    login: str
    senha: str

class UsuarioSchema(UsuarioBase):
    id: int

class UsuarioToken(BaseModel):
    id: int
    nome: str
    login: str
    token: str