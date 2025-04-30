import requests
from typing import Optional
from app.models.empresa import Empresa, Atividade, QSA, Simples, Simei, Billing
from app.core.config import settings

def consulta_cnpj(cnpj: str) -> Optional[Empresa]:
    url = settings.API_URL.format(cnpj)
    
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        
        dados = response.json()
        
        print(f"Dados recebidos: {dados}") 

        if dados.get("status") == "ERROR":
            print(f"Erro na API: {dados.get('message')}")
            return None
            
        return Empresa(
            abertura=dados["abertura"],
            situacao=dados["situacao"],
            tipo=dados["tipo"],
            nome=dados["nome"],
            fantasia=dados["fantasia"],
            porte=dados["porte"],
            natureza_juridica=dados["natureza_juridica"],
            atividade_principal=[Atividade(**atv) for atv in dados["atividade_principal"]],
            qsa=[QSA(**qsa) for qsa in dados["qsa"]],
            logradouro=dados["logradouro"],
            numero=dados["numero"],
            complemento=dados["complemento"],
            municipio=dados["municipio"],
            bairro=dados["bairro"],
            uf=dados["uf"],
            cep=dados["cep"],
            email=dados["email"],
            telefone=dados["telefone"],
            data_situacao=dados["data_situacao"],
            cnpj=dados["cnpj"],
            ultima_atualizacao=dados["ultima_atualizacao"],
            status=dados["status"],
            efr=dados["efr"],
            motivo_situacao=dados["motivo_situacao"],
            situacao_especial=dados["situacao_especial"],
            data_situacao_especial=dados["data_situacao_especial"],
            atividades_secundarias=[Atividade(**atv) for atv in dados["atividades_secundarias"]],
            capital_social=dados["capital_social"],
            simples=Simples(**dados["simples"]),
            simei=Simei(**dados["simei"]),
            extra=dados["extra"],
            billing=Billing(**dados["billing"])
        )
        
    except requests.exceptions.RequestException as e:
        print(f"Erro na requisição: {e}")
        return None
    except KeyError as e:
        print(f"Campo faltando na resposta: {e}")
        return None
    except Exception as e:
        print(f"Erro inesperado: {e}")
        return None