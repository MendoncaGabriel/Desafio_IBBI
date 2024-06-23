from pydantic import BaseModel

class CategoriaEntrada(BaseModel):
    descricao: str

class CategoriaSaida(CategoriaEntrada):
    id: int