import pandas as pd
import re
import networkx as nx

"""
Funções para processar dados de embarque e destino, e gerar grafos a partir desses dados.
"""
def limpar_sobrenome(sobrenome): 
    if pd.isna(sobrenome) or not sobrenome.strip():
        return ""
    sobrenome = re.sub(r'[^\w\sÀ-ú\.]', ' ', sobrenome, flags=re.UNICODE)
    sobrenome = ' '.join(sobrenome.split())
    return sobrenome.strip()

def processar_dados_embarque_destino(caminho_csv):

    df = pd.read_csv(caminho_csv, sep=';', encoding='utf-8', on_bad_lines='warn')
    df = df[['Sobrenome', 'Porto de Embarque', 'Destino']]
    
    df['porto_embarque'] = df['Porto de Embarque'].str.strip()
    df['destino'] = df['Destino'].str.strip()
    
    df['sobrenome_limpo'] = df['Sobrenome'].apply(limpar_sobrenome)
    
    padrao_ilegivel = re.compile(r'\bileg[íi]vel\b', re.IGNORECASE)
    df = df[~df['porto_embarque'].str.contains(padrao_ilegivel.pattern, case=False, na=False)]
    df = df[~df['destino'].str.contains(padrao_ilegivel.pattern, case=False, na=False)]
    df = df[~df['porto_embarque'].str.contains('nada consta', case=False, na=False)]
    
    df = df.dropna(subset=['porto_embarque', 'destino'])
    df = df[(df['sobrenome_limpo'] != "") & 
            (df['porto_embarque'] != "") & 
            (df['destino'] != "")]    
    return df[['sobrenome_limpo', 'porto_embarque', 'destino']].to_dict('records')

def gerar_grafo_scale_free(dados): 
    G = nx.DiGraph()
    for entrada in dados:
        G.add_edge(entrada['sobrenome_limpo'], entrada['porto_embarque'])
        G.add_edge(entrada['porto_embarque'], entrada['destino'])
    return G

def limpar_procedencia(texto): 
    if pd.isna(texto) or not texto.strip():
        return ""
    texto = re.sub(r'[^\w\sÀ-ú\.]', ' ', texto, flags=re.UNICODE)
    texto = ' '.join(texto.split())
    return texto.strip()

def processar_dados_procedencia(caminho_csv): 
    df = pd.read_csv(caminho_csv, sep=';', encoding='utf-8', on_bad_lines='warn')
    df = df[['Procedencia', 'datachegada', 'Porto de Embarque']]

    df['Procedencia'] = df['Procedencia'].apply(limpar_procedencia)
    df['Porto de Embarque'] = df['Porto de Embarque'].str.strip()
    df['datachegada'] = df['datachegada'].str.strip()

    padrao_ilegivel = re.compile(r'\bileg[íi]vel\b', re.IGNORECASE)
    df = df[~df['Procedencia'].str.contains(padrao_ilegivel.pattern, case=False, na=False)]
    df = df[~df['Porto de Embarque'].str.contains(padrao_ilegivel.pattern, case=False, na=False)]
    df = df[~df['Porto de Embarque'].str.contains('nada consta', case=False, na=False)]

    df = df.dropna(subset=['Procedencia', 'Porto de Embarque', 'datachegada'])
    df = df[(df['Procedencia'] != "") & 
            (df['Porto de Embarque'] != "") & 
            (df['datachegada'] != "")]
    return df.to_dict('records')

def gerar_grafo_small_world(dados):  
    G = nx.Graph()
    for entrada in dados:
        G.add_edge(
            entrada['Procedencia'],
            entrada['Porto de Embarque'],
            data_chegada=entrada['datachegada']
        )
    return G

def gerar_grafo_movimento_portos(dados):
    G = nx.DiGraph()

    for entrada in dados:
        embarque = entrada['porto_embarque']
        destino = entrada['destino']
        familia = entrada['sobrenome_limpo']

        if G.has_edge(embarque, destino):
            G[embarque][destino]['peso'] += 1
            G[embarque][destino]['familias'].add(familia)
        else:
            G.add_edge(embarque, destino, peso=1, familias={familia})
    return G

def gerar_grafo_familia_para_europa(dados):
    G = nx.DiGraph()
    for entrada in dados:
        sobrenome = entrada['sobrenome_limpo']
        embarque = entrada['porto_embarque']
        G.add_edge(sobrenome, embarque)
    return G

def gerar_grafo_europa_para_brasil(dados):
    G = nx.DiGraph()
    for entrada in dados:
        embarque = entrada['porto_embarque']
        destino = entrada['destino']
        G.add_edge(embarque, destino)
    return G