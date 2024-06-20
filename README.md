# Desafio IBBI

Este é um projeto desenvolvido como parte do desafio técnico para IBBI.

## Índice

- [Ambiente Virtual](#ambiente-virtual)
- [Solução de Problemas](#solução-de-problemas)
- [Rodar com Docker](#rodar-com-docker)
- [Autenticação](#autenticação)
- [Obtendo Token de Autenticação](#obtendo-token-de-autenticação)
- [Acessando Rotas Restritas](#acessando-rotas-restritas)

## Ambiente Virtual

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
