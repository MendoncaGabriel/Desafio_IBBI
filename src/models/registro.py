from sqlalchemy import Column, Integer, String, Float
from config.database import Base

class Registro(Base):
    __tablename__ = "registros"
    
    id = Column(Integer, primary_key=True, index=True)
    data = Column(String(10))
    hora = Column(String(5))
    descricao_produto = Column(String(255))
    quantidade = Column(Integer)
    produto_id = Column(Integer)
    nome_cliente = Column(String(45))
    nome_vendedor = Column(String(45))
    observacao = Column(String(255))
    valor = Column(Float)
    total = Column(Float)