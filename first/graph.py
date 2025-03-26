import networkx as nx

# Grafo manual simples, não direcionado
def grafo_simples():
    G = nx.Graph()
    G.add_edges_from([
        ('A', 'B'), ('A', 'C'), ('B', 'C'),
        ('C', 'D'), ('D', 'E')
    ])
    return G

# Grafo com direções nas arestas (ex: web, tráfego)
def grafo_direcionado():
    G = nx.DiGraph()
    G.add_edges_from([
        ('A', 'B'), ('B', 'C'), ('C', 'D'),
        ('D', 'E'), ('E', 'A')
    ])
    return G

# Grafo baseado no modelo Barabási-Albert (scale-free)
def grafo_barabasi_albert(n=30, m=2):
    return nx.barabasi_albert_graph(n, m)

# Grafo baseado no modelo Erdős–Rényi (random)
def grafo_random(n=30, p=0.1):
    return nx.erdos_renyi_graph(n, p)

# Grafo do modelo Watts–Strogatz (small-world)
def grafo_small_world(n=30, k=4, p=0.1):
    return nx.watts_strogatz_graph(n, k, p)