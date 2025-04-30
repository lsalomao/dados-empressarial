from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from app.api.endpoints import router
from app.services.database import criar_banco_dados

app = FastAPI(title="Consulta CNPJ API")

# Monta o diretório de arquivos estáticos
app.mount("/static", StaticFiles(directory="static"), name="static")

# Cria o banco de dados na inicialização
criar_banco_dados()

# Registra os endpoints
app.include_router(router, prefix="/api", tags=["CNPJ"])

@app.get("/")
async def root():
    return FileResponse("static/index.html")