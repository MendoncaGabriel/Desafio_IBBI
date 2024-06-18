# Desafio_IBBI
    Projeto de desafio para teste técnico IBBI

# Entre no ambiente Venv
    .\venv\Scripts\activate 

# Instale as dependencias do projeto usando o seguinte comando
    pip install -r requirements.txt

# Execute o sistema com o seguinte codigo
    uvicorn src.main:app --reload

# Em caso de falha siga os passos
# 1 - Desative e exclua o ambiente virtual existente.
    deactivate  # se estiver ativo
    Remove-Item -Recurse -Force venv

# 2 - Crie um novo anbiente virtual
    python -m venv venv
    .\venv\Scripts\Activate.ps1  # para PowerShell
