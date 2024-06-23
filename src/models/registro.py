from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from config.database import Base

class Registro(Base):
    __tablename__ = "registros"
    
    id = Column(Integer, primary_key=True, index=True)
    data = Column(DateTime)
    observacao = Column(String(255))
    quantidade = Column(Integer)
    nome_cliente = Column(String(255))
    
    # Chaves estrangeiras para relacionamentos
    usuario_id = Column(Integer, ForeignKey('usuarios.id'))
    produto_id = Column(Integer, ForeignKey("produtos.id"))
    
    # Relacionamentos com Usuario e Produto
    usuario = relationship("Usuario", back_populates="registros")
    produto = relationship("Produto", back_populates="registros")
