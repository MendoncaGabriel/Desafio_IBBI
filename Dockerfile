# Imagem oficial do Python
FROM python:3.12

# Diretorio raiz do projeto
WORKDIR /src

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

# Exponha a porta que a aplicação ira usar
EXPOSE 8000

# Comando para rodar a aplicação
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
