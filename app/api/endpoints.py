from fastapi import APIRouter, HTTPException
from app.services.cnpj_service import consulta_cnpj
from app.services.database import salvar_empresa
from app.schemas.empresa_schema import EmpresaSchema
from app.models.empresa import Empresa

router = APIRouter()

@router.get("/cnpj/{cnpj}", response_model=EmpresaSchema)
async def consultar_cnpj(cnpj: str):
    """
    Consulta os dados de uma empresa pelo CNPJ e salva no banco de dados.
    
    Args:
        cnpj (str): CNPJ da empresa a ser consultada.
        
    Returns:
        EmpresaSchema: Dados da empresa.
        
    Raises:
        HTTPException: Se a consulta falhar ou o CNPJ for inválido.
    """
    empresa: Empresa = consulta_cnpj(cnpj)
    
    if not empresa:
        raise HTTPException(status_code=404, detail="CNPJ não encontrado ou erro na consulta")
    
    salvar_empresa(empresa)
    return empresa