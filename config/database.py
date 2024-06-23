from dotenv import load_dotenv, find_dotenv
import os
import pymysql
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Carrega variáveis de ambiente do arquivo .env
load_dotenv(find_dotenv())

# Configuração das variáveis de ambiente
DB_USER = os.getenv('DB_USER')
DB_PASS = os.getenv('DB_PASS')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_NAME = os.getenv('DB_NAME')

# String de conexão MySQL
connection_string = f'mysql+pymysql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}'

# Cria a engine do SQLAlchemy
engine = create_engine(connection_string)

# Cria uma sessão do SQLAlchemy
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para a definição dos modelos
Base = declarative_base()

# Função para retornar uma instância de sessão do SQLAlchemy. A sessão é fechada automaticamente ao final do uso.
def get_db():
    with SessionLocal() as db:
        yield db
