from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

USER = 'root'
PASSWORD = '22052719'
HOST = 'localhost'  
PORT = '3306'
DATABASE = 'ibbi'

# String de conexão 
connection_string = f'mysql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}'

# Cria a engine do SQLAlchemy
engine = create_engine(connection_string)

# Cria uma sessão do SQLAlchemy
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para a definição dos modelos
Base = declarative_base()
