import networkx as nx
import pandas as pd

# Métricas locais por nó: grau, centralidades, clustering
def calcular_metricas(grafo):
    if isinstance(grafo, nx.DiGraph):
        grau = dict(grafo.out_degree())  # Direcionado: out_degree
    else:
        grau = dict(grafo.degree())

    metricas = {
        "grau": grau,
        "centralidade_grau": nx.degree_centrality(grafo),
        "centralidade_intermediacao": nx.betweenness_centrality(grafo),
        "centralidade_proximidade": nx.closeness_centrality(grafo)
    }

    if not isinstance(grafo, nx.DiGraph):
        metricas["clustering"] = nx.clustering(grafo)

    return pd.DataFrame(metricas)

# Métricas globais: densidade, diâmetro, caminho médio, clustering médio
def metricas_globais(grafo):
    globais = {
        "nós": grafo.number_of_nodes(),
        "arestas": grafo.number_of_edges(),
        "densidade": round(nx.density(grafo), 3)
    }

    if nx.is_connected(grafo.to_undirected()):
        globais["diâmetro"] = nx.diameter(grafo.to_undirected())
        globais["caminho_médio"] = round(nx.average_shortest_path_length(grafo.to_undirected()), 3)

    if not isinstance(grafo, nx.DiGraph):
        globais["clustering_médio"] = round(nx.average_clustering(grafo), 3)

    return globais

# Métricas estruturais: excentricidade, raio e centro (centralidade baseada em distância máxima)
def propriedades_estruturais(grafo):
    if not nx.is_connected(grafo.to_undirected()):
        return "O grafo não é conectado."

    excentricidade = nx.eccentricity(grafo)
    raio = nx.radius(grafo)
    centro = nx.center(grafo)

    return {
        "excentricidade": excentricidade,
        "raio": raio,
        "centro": centro
    }