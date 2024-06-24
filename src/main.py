from fastapi import FastAPI
from src.routers import produtos, categorias, usuario, registro
from config.database import engine, Base
import os
from fastapi.responses import RedirectResponse



ENV_PORT = os.getenv("ENV_PORT")
ENV_HOST = os.getenv("ENV_HOST")

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/", include_in_schema=False)
async def root():
    return RedirectResponse(url="/docs")

# Rotas
app.include_router(produtos.router, prefix="/produto", tags=["Produto"])
app.include_router(categorias.router, prefix="/categoria", tags=["Categoria"])
app.include_router(usuario.router, prefix="/usuario", tags=["Usuário"])
app.include_router(registro.router, prefix="/registro", tags=["Registro"])

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host=ENV_HOST, port=ENV_PORT)
