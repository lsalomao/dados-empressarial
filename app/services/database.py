import sqlite3
from app.models.empresa import Empresa
from app.core.config import settings

def criar_banco_dados():
    """Cria as tabelas no banco SQLite"""
    conn = sqlite3.connect(settings.DATABASE_PATH)
    cursor = conn.cursor()
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS empresas (
        cnpj TEXT PRIMARY KEY,
        nome TEXT NOT NULL,
        fantasia TEXT,
        abertura TEXT,
        situacao TEXT,
        tipo TEXT,
        porte TEXT,
        natureza_juridica TEXT,
        logradouro TEXT,
        numero TEXT,
        complemento TEXT,
        municipio TEXT,
        bairro TEXT,
        uf TEXT,
        cep TEXT,
        email TEXT,
        telefone TEXT,
        data_situacao TEXT,
        ultima_atualizacao TEXT,
        status TEXT,
        efr TEXT,
        motivo_situacao TEXT,
        situacao_especial TEXT,
        data_situacao_especial TEXT,
        capital_social REAL
    )
    ''')
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS atividades_principais (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        cnpj_empresa TEXT,
        code TEXT,
        text TEXT,
        FOREIGN KEY (cnpj_empresa) REFERENCES empresas (cnpj)
    )
    ''')
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS atividades_secundarias (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        cnpj_empresa TEXT,
        code TEXT,
        text TEXT,
        FOREIGN KEY (cnpj_empresa) REFERENCES empresas (cnpj)
    )
    ''')
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS qsa (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        cnpj_empresa TEXT,
        nome TEXT,
        qual TEXT,
        FOREIGN KEY (cnpj_empresa) REFERENCES empresas (cnpj)
    )
    ''')
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS simples (
        cnpj_empresa TEXT PRIMARY KEY,
        optante BOOLEAN,
        data_opcao TEXT,
        data_exclusao TEXT,
        ultima_atualizacao TEXT,
        FOREIGN KEY (cnpj_empresa) REFERENCES empresas (cnpj)
    )
    ''')
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS simei (
        cnpj_empresa TEXT PRIMARY KEY,
        optante BOOLEAN,
        data_opcao TEXT,
        data_exclusao TEXT,
        ultima_atualizacao TEXT,
        FOREIGN KEY (cnpj_empresa) REFERENCES empresas (cnpj)
    )
    ''')
    
    conn.commit()
    conn.close()

def salvar_empresa(empresa: Empresa):
    """Salva todos os dados da empresa no banco SQLite"""
    conn = sqlite3.connect(settings.DATABASE_PATH)
    cursor = conn.cursor()
    
    try:
        cursor.execute('''
        INSERT OR REPLACE INTO empresas VALUES (
            :cnpj, :nome, :fantasia, :abertura, :situacao, :tipo, :porte,
            :natureza_juridica, :logradouro, :numero, :complemento,
            :municipio, :bairro, :uf, :cep, :email, :telefone,
            :data_situacao, :ultima_atualizacao, :status, :efr,
            :motivo_situacao, :situacao_especial, :data_situacao_especial,
            :capital_social
        )
        ''', {
            'cnpj': empresa.cnpj,
            'nome': empresa.nome,
            'fantasia': empresa.fantasia,
            'abertura': empresa.abertura,
            'situacao': empresa.situacao,
            'tipo': empresa.tipo,
            'porte': empresa.porte,
            'natureza_juridica': empresa.natureza_juridica,
            'logradouro': empresa.logradouro,
            'numero': empresa.numero,
            'complemento': empresa.complemento,
            'municipio': empresa.municipio,
            'bairro': empresa.bairro,
            'uf': empresa.uf,
            'cep': empresa.cep,
            'email': empresa.email,
            'telefone': empresa.telefone,
            'data_situacao': empresa.data_situacao,
            'ultima_atualizacao': empresa.ultima_atualizacao,
            'status': empresa.status,
            'efr': empresa.efr,
            'motivo_situacao': empresa.motivo_situacao,
            'situacao_especial': empresa.situacao_especial,
            'data_situacao_especial': empresa.data_situacao_especial,
            'capital_social': float(empresa.capital_social) if empresa.capital_social else None
        })
        
        for atv in empresa.atividade_principal:
            cursor.execute('''
            INSERT INTO atividades_principais (cnpj_empresa, code, text)
            VALUES (?, ?, ?)
            ''', (empresa.cnpj, atv.code, atv.text))
        
        for atv in empresa.atividades_secundarias:
            cursor.execute('''
            INSERT INTO atividades_secundarias (cnpj_empresa, code, text)
            VALUES (?, ?, ?)
            ''', (empresa.cnpj, atv.code, atv.text))
        
        for socio in empresa.qsa:
            cursor.execute('''
            INSERT INTO qsa (cnpj_empresa, nome, qual)
            VALUES (?, ?, ?)
            ''', (empresa.cnpj, socio.nome, socio.qual))
        
        cursor.execute('''
        INSERT OR REPLACE INTO simples VALUES (
            ?, ?, ?, ?, ?
        )
        ''', (
            empresa.cnpj,
            empresa.simples.optante,
            empresa.simples.data_opcao,
            empresa.simples.data_exclusao,
            empresa.simples.ultima_atualizacao
        ))
        
        cursor.execute('''
        INSERT OR REPLACE INTO simei VALUES (
            ?, ?, ?, ?, ?
        )
        ''', (
            empresa.cnpj,
            empresa.simei.optante,
            empresa.simei.data_opcao,
            empresa.simei.data_exclusao,
            empresa.simei.ultima_atualizacao
        ))
        
        conn.commit()
        print(f"Dados da empresa {empresa.nome} salvos com sucesso!")
        
    except sqlite3.Error as e:
        print(f"Erro ao salvar no banco de dados: {e}")
        conn.rollback()
        
    finally:
        conn.close()