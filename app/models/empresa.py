from dataclasses import dataclass
from typing import List, Dict, Optional
from datetime import datetime

@dataclass
class Atividade:
    code: str
    text: str

@dataclass
class QSA:
    nome: str
    qual: str

@dataclass
class Simples:
    optante: bool
    data_opcao: Optional[str]
    data_exclusao: Optional[str]
    ultima_atualizacao: str

@dataclass
class Simei:
    optante: bool
    data_opcao: Optional[str]
    data_exclusao: Optional[str]
    ultima_atualizacao: str

@dataclass
class Billing:
    free: bool
    database: bool

@dataclass
class Empresa:
    abertura: str
    situacao: str
    tipo: str
    nome: str
    fantasia: str
    porte: str
    natureza_juridica: str
    atividade_principal: List[Atividade]
    qsa: List[QSA]
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
    atividades_secundarias: List[Atividade]
    capital_social: str
    simples: Simples
    simei: Simei
    extra: Dict
    billing: Billing

    @property
    def data_abertura_formatada(self) -> Optional[datetime]:
        try:
            return datetime.strptime(self.abertura, "%d/%m/%Y")
        except:
            return None