from fastapi import FastAPI
from src.routers import produtos, categorias, usuario
from src.config.database import engine, Base
import os

ENV_PORT = os.getenv("ENV_PORT")
ENV_HOST = os.getenv("ENV_HOST")

Base.metadata.create_all(bind=engine)

app = FastAPI()

# Routes
app.include_router(produtos.router, prefix="/produto", tags=["Produto"])
app.include_router(categorias.router, prefix="/categoria", tags=["Categoria"])
app.include_router(usuario.router, prefix="/usuario", tags=["Usuário"])

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host=ENV_HOST, port=ENV_PORT)
