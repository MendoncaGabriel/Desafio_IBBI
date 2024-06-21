# Desafio Técnico IBBI
Este é um projeto desenvolvido como parte do desafio técnico para IBBI.
O objetivo e criar um sistema para controle de vendas de um e-commerce.

## Índice
- [Ambiente Virtual](#ambiente-virtual)
- [Solução de Problemas](#solução-de-problemas)
- [Rodar com Docker](#rodar-com-docker)
- [Autenticação](#autenticação)
- [Obtendo Token de Autenticação](#obtendo-token-de-autenticação)
- [Acessando Rotas Restritas](#acessando-rotas-restritas)

## Ambiente Virtual
**1 - Crie um ambiente vitual usando:**
python -m venv venv

**2 - Ative o novo ambiente virtual:**
.\venv\Scripts\activate

**3 - Instale o uvicorn**
pip install uvicorn

**4 - instale as dependecias do projeto:**
pip install -r requirements.txt

**5 - Execute o sistema:**
uvicorn src.main:app --reload  

**Observações:**
Caso escolha executar o sistema via ambiente virtual, e importante garantir um servidor Mysql e configurar corretamente as variaveis de ambiente no arquivo .env
- [Erro de conexão com banco de dados](#erro-conexao-com-banco-de-dados)


### Ativar Ambiente Virtual

Para ativar o ambiente virtual:

.\venv\Scripts\activate

### Instalar Dependências

Para instalar as dependências do projeto:

pip install -r requirements.txt

### Executar o Projeto

Para executar o projeto em ambiente virtual:

uvicorn src.main:app --reload

## Solução de Problemas

## Erro conexao com banco de dados
Em caso de erro com conexão com banco de dados ou variaveis de ambiente desatualizadas, abra a pasta ./src/config e apague a pasta __pycache__ dentro dela.

Se ocorrerem problemas durante a execução, siga estes passos:

1. Desativar e Excluir o Ambiente Virtual Existente:

deactivate  # se estiver ativo
Remove-Item -Recurse -Force venv

2. Criar e Ativar um Novo Ambiente Virtual:

python -m venv venv
.\venv\Scripts\activate

## Rodar com Docker

Para rodar o projeto utilizando Docker, execute o seguinte comando:

docker-compose up --build

## Autenticação

### Obtendo Token de Autenticação

Para obter um token de autenticação, faça uma requisição para /usuario/signup ou /usuario/signin.

### Acessando Rotas Restritas

Para acessar rotas protegidas, adicione o seguinte cabeçalho à sua requisição HTTP:

Authorization: Bearer <seu-token-aqui>

Substitua <seu-token-aqui> pelo token obtido na autenticação.

## Cadastro

1 - Cadastre uma categoria informando uma descricao para o endpoint: POST /categoria/
2 - Cadastro um produto informando os seguintes campos
{
  "descricao": "string",
  "valor": 0,
  "quantidade": 0,
  "categoria_id": 1
}

Observação: O campo "categoria_id" e obrigatorio para manter o relacionamento entre as tabelas de categoria e produto