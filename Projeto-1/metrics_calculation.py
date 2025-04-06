import networkx as nx 
import logging

"""
Funções para calcular e exibir métricas de grafos.
"""
def calcular_metricas(G): 
    metrics = {}
    G_undirected = nx.Graph(G)
    
    metrics["Número de Nós"] = G.number_of_nodes()
    metrics["Número de Arestas"] = G.number_of_edges()
    logging.info(f"Nós: {metrics['Número de Nós']}, Arestas: {metrics['Número de Arestas']}")
    
    is_connected = nx.is_connected(G_undirected)
    metrics["Conectividade"] = "Conectado" if is_connected else "Desconexo"
    metrics["Número de Componentes"] = nx.number_connected_components(G_undirected)
    metrics["Componentes Conexas (Detalhados)"] = [list(c) for c in nx.connected_components(G_undirected)]
    metrics["Componente Gigante (Tamanho)"] = max(len(c) for c in nx.connected_components(G_undirected))
    logging.info(f"Conectividade: {metrics['Conectividade']}, Componentes: {metrics['Número de Componentes']}")
    
    try:
        metrics["Centralidade de Grau (Top 5)"] = sorted(
            nx.degree_centrality(G).items(), 
            key=lambda x: -x[1]
        )[:5]
    except Exception as e:
        logging.error(f"Erro na Centralidade de Grau: {str(e)}")
        metrics["Centralidade de Grau (Top 5)"] = "Erro"
    
    try:
        metrics["Centralidade de Entrementes (Top 5)"] = sorted(
            nx.betweenness_centrality(G).items(), 
            key=lambda x: -x[1]
        )[:5]
    except Exception as e:
        logging.error(f"Erro na Centralidade de Entrementes: {str(e)}")
        metrics["Centralidade de Entrementes (Top 5)"] = "Erro"
    
    try:
        metrics["Centralidade de Proximidade (Top 5)"] = sorted(
            nx.closeness_centrality(G).items(), 
            key=lambda x: -x[1]
        )[:5]
    except Exception as e:
        logging.error(f"Erro na Centralidade de Proximidade: {str(e)}")
        metrics["Centralidade de Proximidade (Top 5)"] = "Erro"
    
    if is_connected:
        try:
            metrics["Diâmetro"] = nx.diameter(G_undirected)
        except Exception as e:
            logging.error(f"Erro no Diâmetro: {str(e)}")
            metrics["Diâmetro"] = "Erro"
        
        try:
            metrics["Distância Média"] = nx.average_shortest_path_length(G_undirected)
        except Exception as e:
            logging.error(f"Erro na Distância Média: {str(e)}")
            metrics["Distância Média"] = "Erro"
        
        try:
            metrics["Coeficiente de Aglomeração Médio"] = nx.average_clustering(G_undirected)
        except Exception as e:
            logging.error(f"Erro no Coeficiente de Aglomeração: {str(e)}")
            metrics["Coeficiente de Aglomeração Médio"] = "Erro"
    else:
        metrics.update({
            "Diâmetro": "Grafo desconexo",
            "Distância Média": "Grafo desconexo",
            "Coeficiente de Aglomeração Médio": "Grafo desconexo"
        })
    
    metrics["Densidade da Rede"] = nx.density(G)
    return metrics

def exibir_metricas(metrics):
    print("\n" + "="*50)
    print("** ANÁLISE DA REDE **".center(50))
    print("="*50 + "\n")
    
    for key, value in metrics.items():
        print(f"► {key}:")
        
        if isinstance(value, list):
            for item in value:
                if isinstance(item, tuple):
                    nome, valor = item
                    print(f"   - {nome}: {valor:.4f}" if isinstance(valor, float) else f"   - {nome}: {valor}")
                else:
                    print(f"   - {item}")
        else:
            print(f"   {value}")
        
        print("-"*50)