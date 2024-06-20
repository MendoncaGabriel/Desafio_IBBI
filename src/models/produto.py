from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from src.config.database import Base

class Produto(Base):
    __tablename__ = "produtos"

    id = Column(Integer, primary_key=True, unique=True, index=True)
    descricao = Column(String(255), unique=True, index=True)
    valor = Column(Float)
    quantidade = Column(Integer, index=True)
    categoria_id = Column(Integer, ForeignKey("categorias.id"))

    # Relacionamento com categoria
    categoria = relationship("Categoria", back_populates="produtos")

