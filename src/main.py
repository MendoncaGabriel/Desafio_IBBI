from fastapi import FastAPI
from src.routers import produtos, categorias
from src.config.database import engine, Base
import os

ENV_PORT = os.getenv("PORT", "8000")
ENV_HOST = os.getenv("HOST", "0.0.0.0")

Base.metadata.create_all(bind=engine)

app = FastAPI()

# Routes
app.include_router(produtos.router, prefix="/produto", tags=["Produto"])
app.include_router(categorias.router, prefix="/categoria", tags=["Categoria"])

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host=ENV_HOST, port=ENV_PORT)
