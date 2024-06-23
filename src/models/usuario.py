from sqlalchemy import Column, Integer, String
from config.database import Base
from sqlalchemy.orm import relationship


class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, unique=True, index=True)
    nome = Column(String(255), unique=True, index=True)
    login = Column(String(255), unique=True, index=True)
    senha = Column(String(255))

    # Relacionamentos
    registros = relationship("Registro", back_populates="usuario")
    
