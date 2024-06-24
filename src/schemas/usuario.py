from pydantic import BaseModel

class UsuarioEntrada(BaseModel):
    nome: str
    login: str
    senha: str

class UsuarioLogin(BaseModel):
    login: str
    senha: str   

class UsuarioSaida(BaseModel):
    id: int
    token: str
    
class UsuarioRemove(BaseModel):
    msg: str