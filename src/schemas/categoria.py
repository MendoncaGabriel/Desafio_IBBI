from pydantic import BaseModel

class CategoriaBase(BaseModel):
    descricao: str
    
class CategoriaCreate(CategoriaBase):
    pass

class CategoriaSchema(CategoriaBase):
    id: int
    
    class Config:
        orm_mode = True
