from sqlalchemy import Column, Integer, String
from src.config.database import Base

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(255), index=True)
    login = Column(String(255), unique=True, index=True)
    senha = Column(String(255))
