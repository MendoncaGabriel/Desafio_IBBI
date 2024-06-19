from fastapi import FastAPI
from src.routers import produtos, categorias
from src.config.database import engine, Base

# Importa a configuração do SQLAlchemy e inicializa o banco de dados
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Routes
app.include_router(produtos.router, prefix="/produto", tags=["Produto"])
app.include_router(categorias.router, prefix="/categoria", tags=["Categoria"])

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
