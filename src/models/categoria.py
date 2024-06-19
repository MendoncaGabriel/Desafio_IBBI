from sqlalchemy import Column, Integer, String
from src.config.database import Base

class Categoria(Base):
    __tablename__ = "categorias"
    
    id = Column(Integer, primary_key=True, index=True)
    descricao = Column(String(255), index=True)