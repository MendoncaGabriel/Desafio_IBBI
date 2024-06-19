# Use uma imagem oficial do Python
FROM python:3.12

# Defina o diretório de trabalho
WORKDIR /src

# Copie o arquivo de requisitos
COPY requirements.txt .

# Instale as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copie o restante do código da aplicação
COPY . .

# Defina a variável de ambiente para a URL do banco de dados
ENV DATABASE_URL=mysql+pymysql://root:22052719@localhost/ibbi

# Exponha a porta que a aplicação irá usar
EXPOSE 8000

# Comando para rodar a aplicação
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
