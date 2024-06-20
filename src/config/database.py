from dotenv import load_dotenv, find_dotenv  
import os
import pymysql
pymysql.install_as_MySQLdb()

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv(find_dotenv())
 
# Pega as informações das variáveis de ambiente
ENV_DB_USER = os.getenv('DB_USER')
ENV_DB_PASS = os.getenv('DB_PASS')
ENV_DB_HOST = os.getenv('DB_HOST')
ENV_DB_PORT = os.getenv('DB_PORT')
ENV_DB_NAME = os.getenv('DB_NAME')

print("_____________________________")
print(f"VARIAVEIS DE AMBIENTE: || user: {ENV_DB_USER}, pass: {ENV_DB_PASS}, host: {ENV_DB_HOST}, port: {ENV_DB_PORT}, name: {ENV_DB_NAME}")
print("_____________________________")
 
# ENV_DB_USER = "root"
# ENV_DB_PASS = 22052719
# ENV_DB_HOST = "localhost"
# ENV_DB_PORT = 3306
# ENV_DB_NAME = "ibbi"

# String de conexão
connection_string = f'mysql+pymysql://{ENV_DB_USER}:{ENV_DB_PASS}@{ENV_DB_HOST}:{ENV_DB_PORT}/{ENV_DB_NAME}'

# Cria a engine do SQLAlchemy
engine = create_engine(connection_string)

# Cria uma sessão do SQLAlchemy
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para a definição dos modelos
Base = declarative_base()
