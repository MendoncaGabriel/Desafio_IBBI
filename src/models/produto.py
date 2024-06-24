from sqlalchemy import Column, Integer, String, Float, Text, ForeignKey
from sqlalchemy.orm import relationship
from config.database import Base

class Produto(Base):
    __tablename__ = "produtos"

    id = Column(Integer, primary_key=True, unique=True, index=True)
    descricao = Column(String(255), unique=True, index=True)
    valor = Column(Float)
    quantidade = Column(Integer)
    categoria_id = Column(Integer, ForeignKey("categorias.id"))
    imagem = Column(Text, default="")
    venda = Column(Integer, default=0)

    # Relacionamentos
    categoria = relationship("Categoria", back_populates="produtos")
