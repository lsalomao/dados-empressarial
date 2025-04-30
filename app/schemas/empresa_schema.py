from pydantic import BaseModel
from typing import List, Dict, Optional
from datetime import datetime

class AtividadeSchema(BaseModel):
    code: str
    text: str

class QSASchema(BaseModel):
    nome: str
    qual: str

class SimplesSchema(BaseModel):
    optante: bool
    data_opcao: Optional[str]
    data_exclusao: Optional[str]
    ultima_atualizacao: str

class SimeiSchema(BaseModel):
    optante: bool
    data_opcao: Optional[str]
    data_exclusao: Optional[str]
    ultima_atualizacao: str

class BillingSchema(BaseModel):
    free: bool
    database: bool

class EmpresaSchema(BaseModel):
    abertura: str
    situacao: str
    tipo: str
    nome: str
    fantasia: str
    porte: str
    natureza_juridica: str
    atividade_principal: List[AtividadeSchema]
    qsa: List[QSASchema]
    logradouro: str
    numero: str
    complemento: str
    municipio: str
    bairro: str
    uf: str
    cep: str
    email: str
    telefone: str
    data_situacao: str
    cnpj: str
    ultima_atualizacao: str
    status: str
    efr: str
    motivo_situacao: str
    situacao_especial: str
    data_situacao_especial: str
    atividades_secundarias: List[AtividadeSchema]
    capital_social: str
    simples: SimplesSchema
    simei: SimeiSchema
    extra: Dict
    billing: BillingSchema
    data_abertura_formatada: Optional[datetime]

    class Config:
        from_attributes = True