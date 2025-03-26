import matplotlib.pyplot as plt
import networkx as nx
from collections import Counter

# Desenha o grafo com layout e rótulos
def mostrar_grafo(grafo, titulo="Grafo"):
    plt.figure(figsize=(8, 6))
    pos = nx.spring_layout(grafo, seed=42)
    nx.draw(grafo, pos, with_labels=True, node_size=700,
            node_color='skyblue', font_size=12, edge_color='gray')
    plt.title(titulo)
    plt.show()

# Exibe o histograma da distribuição de grau dos nós
def plotar_distribuicao_de_grau(grafo, titulo="Distribuição de Grau"):
    graus = [d for _, d in grafo.degree()]
    contagem = Counter(graus)

    x = list(contagem.keys())
    y = list(contagem.values())

    plt.figure()
    plt.bar(x, y, color='steelblue')
    plt.xlabel("Grau")
    plt.ylabel("Número de Nós")
    plt.title(titulo)
    plt.grid(True)
    plt.show()

# Destaca visualmente o(s) nó(s) do centro (menor excentricidade)
def mostrar_centro(grafo, titulo="Centro do Grafo"):
    if not nx.is_connected(grafo.to_undirected()):
        print("Grafo desconectado. Não é possível determinar o centro.")
        return

    centro = nx.center(grafo)
    pos = nx.spring_layout(grafo, seed=42)

    plt.figure(figsize=(8, 6))
    node_colors = ['orange' if node in centro else 'skyblue' for node in grafo.nodes()]
    nx.draw(grafo, pos, with_labels=True, node_color=node_colors,
            edge_color='gray', node_size=700, font_size=12)
    plt.title(titulo + f" - Centro: {centro}")
    plt.show()