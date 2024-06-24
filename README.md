# Desafio Técnico: IBBI - Instituto Brasileiro de Biotecnologia e Inovação

## Introdução
Este projeto foi desenvolvido como parte de um desafio técnico do Instituto IBBI e tem como objetivo a criação de uma aplicação para controle de vendas em um e-commerce.

## Tecnologias Utilizadas
- Python
- MySQL
- Docker
- SQLAlchemy
- Pydantic
- JSON Web Token (JWT)
- Bcrypt


## Instalação

### Ambiente Virtual com Uvicorn
1. Crie um ambiente virtual utilizando o comando: `python -m venv venv`
2. Ative o ambiente virtual: `.\venv\Scripts\activate`
3. Instale o Uvicorn: `pip install uvicorn`
4. Instale as dependências do projeto: `pip install -r requirements.txt`
5. Siga as [etapas de execução](#via-uvcorn).

### Observações

Para executar o programa via Uvicorn, é necessário ter o Python 3 instalado e um SGBD MySQL configurado corretamente nas variáveis de ambiente no arquivo `.env`.

## Ambiente Docker

Para executar o projeto via Docker, é necessário ter o Docker e o docker-compose instalados em seu computador. Abra o Docker Desktop e siga as [etapas de execução](#via-docker).

## Executando a Aplicação

### Via Uvicorn:
1. Execute o programa: `uvicorn src.main:app`
   - Experimente usar a flag `--reload` para ter o Hot Reload.
2. Acesse a documentação da API no Swagger neste endereço: [http://localhost:8000/docs](http://localhost:8000/docs)

### Via Docker
1. Execute o comando de build no terminal: `docker-compose up --build`
2. Acesse a documentação da API no Swagger neste endereço: [http://localhost:3000/docs](http://localhost:3000/docs)


## Estrutura do Projeto
.
├── config
│   ├── database.py       # Configurações de conexão com o banco de dados
├── src
│   ├── controllers
│   │   ├── categoria.py   # Controlador para operações relacionadas a categorias
│   │   ├── produto.py     # Controlador para operações relacionadas a produtos
│   │   ├── registro.py    # Controlador para operações relacionadas a registros
│   │   ├── usuario.py     # Controlador para operações relacionadas a usuários
│   ├── models
│   │   ├── categoria.py   # Modelos de dados para categorias
│   │   ├── produto.py     # Modelos de dados para produtos
│   │   ├── registro.py    # Modelos de dados para registros
│   │   ├── usuario.py     # Modelos de dados para usuários
│   ├── routers
│   │   ├── categoria.py   # Rotas da API para categorias
│   │   ├── produto.py     # Rotas da API para produtos
│   │   ├── registro.py    # Rotas da API para registros
│   │   ├── usuario.py     # Rotas da API para usuários
│   ├── schemas
│   │   ├── categoria.py   # Esquemas de validação para categorias
│   │   ├── produto.py     # Esquemas de validação para produtos
│   │   ├── registro.py    # Esquemas de validação para registros
│   │   ├── usuario.py     # Esquemas de validação para usuários
│   ├── utilities
│   │   ├── auth.py        # Funções utilitárias para autenticação
│   │   ├── converter.py   # Funções utilitárias para conversão de dados
├── tests
│   ├── __init__.py        # Arquivo de inicialização para os testes
│   ├── test_categorias.py # Testes para o módulo de categorias
│   ├── test_docs.py       # Testes para a documentação da API
│   ├── test_produto.py    # Testes para o módulo de produtos
│   ├── test_registro.py   # Testes para o módulo de registros
│   ├── test_usuario.py    # Testes para o módulo de usuários
├── .env                   # Arquivo dotenv para armazenamento de variáveis de ambiente
├── .gitattributes
├── docker-compose.yml
├── Dockerfile
└── README.md              # Este arquivo, contendo a documentação do projeto


## Endpoints da API

Para utilizar os endpoints da API, é necessário obter uma chave de autenticação. Esta chave pode ser facilmente obtida ao criar uma conta de usuário ou realizar o login. No diretório `/docs`, localizado no canto superior direito, há um botão que abre um formulário. Copie o token de autenticação e cole no campo HTTPBearer Value do formulário, em seguida, confirme clicando no botão Authorize.

### Produtos

- **POST** `/produto/` - Cria um novo produto.
- **GET** `/produto/` - Retorna todos os produtos.
- **GET** `/produto/getbycategoria` - Retorna produtos por categoria.
- **GET** `/produto/mais_vendidos` - Retorna os produtos mais vendidos.
- **GET** `/produto/descricao` - Retorna descrições dos produtos.
- **GET** `/produto/{id}` - Retorna um produto específico pelo ID.
- **PUT** `/produto/{id}` - Atualiza um produto pelo ID.
- **DELETE** `/produto/{id}` - Deleta um produto pelo ID.

### Categorias

- **POST** `/categoria/` - Cria uma nova categoria.
- **GET** `/categoria/` - Retorna todas as categorias.
- **GET** `/categoria/{id}` - Retorna uma categoria específica pelo ID.
- **PUT** `/categoria/{id}` - Atualiza uma categoria pelo ID.
- **DELETE** `/categoria/{id}` - Deleta uma categoria pelo ID.

### Usuários

- **POST** `/usuario/signup` - Registra um novo usuário.
- **POST** `/usuario/login` - Realiza o login de um usuário.
- **DELETE** `/usuario/{id}` - Deleta um usuário pelo ID.

### Registros

- **POST** `/registro/` - Registra uma nova entrada.
- **GET** `/registro/ultimas-vendas` - Retorna as últimas vendas registradas.
- **DELETE** `/registro/ultimas-vendas` - Deleta as últimas vendas registradas.

## Testes

Para executar os testes unitários da aplicação, utilize o comando no terminal: `pytest`

### Observação Importante

Antes de executar os testes, é necessário comentar ou remover a dependência de segurança (security: dict = Depends(checkAuthorization)) de todas as rotas da API. Isso permite que os testes sejam realizados sem a necessidade de autenticação, garantindo uma cobertura completa dos casos de teste durante o processo de teste automatizado.

### Como Comentar ou Remover a Dependência de Segurança

1. Localize as Rotas: Abra os arquivos de roteamento (`routers/*.py`) onde as rotas da API estão definidas.

2. Comente ou Remova a Linha de Segurança: Procure por trechos de código que incluam a dependência de segurança `security: dict = Depends(checkAuthorization)`. Comente ou remova essa linha temporariamente para desabilitar a verificação de autenticação durante os testes.

3. Execute os Testes: Após comentar ou remover as dependências de segurança, execute os testes novamente utilizando o comando `pytest` para verificar o funcionamento correto de todas as funcionalidades da API em um ambiente de teste.



## Agradecimentos

Gostaria de agradecer ao Instituto [IBBI](https://www.ibbi.org.br/) pela oportunidade de participar deste desafio técnico, que certamente contribuirá significativamente para o meu desenvolvimento profissional.

### Gabriel Andrade - Desenvolvedor

Email: mendoncagabriel1997@gmail.com