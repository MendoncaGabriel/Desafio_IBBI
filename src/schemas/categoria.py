from pydantic import BaseModel

class CategoriaBase(BaseModel):
    descricao: str

class CategoriaSchema(CategoriaBase):
    id: int