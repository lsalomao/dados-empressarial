from fastapi import FastAPI
from app.api.endpoints import router
from app.services.database import criar_banco_dados

app = FastAPI(title="Consulta CNPJ API")

# Cria o banco de dados na inicialização
criar_banco_dados()

# Registra os endpoints
app.include_router(router, prefix="/api", tags=["CNPJ"])

@app.get("/")
async def root():
    return {"message": "Bem-vindo à API de Consulta de CNPJ"}