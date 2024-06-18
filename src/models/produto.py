from sqlalchemy import Column, Integer, String, Float
from src.config.database import Base

class Produto(Base):
    __tablename__ = "produtos"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(255), index=True)
    descricao = Column(String(255), index=True)
    preco = Column(Float, index=True)
