from dotenv import load_dotenv, find_dotenv
import os
from sqlalchemy import create_engine
from sqlalchemy.orm  import declarative_base
from sqlalchemy.orm import sessionmaker

load_dotenv(find_dotenv())

DB_USER = os.getenv('DB_USER')
DB_PASS = os.getenv('DB_PASS')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_NAME = os.getenv('DB_NAME')

connection_string = f'mysql+pymysql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}'

engine = create_engine(connection_string)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para a definição dos modelos
Base = declarative_base()

# Função para retornar uma instância de sessão, a sessão é fechada automaticamente apos o uso.
def get_db():
    with SessionLocal() as db:
        yield db
