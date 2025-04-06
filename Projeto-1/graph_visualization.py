import networkx as nx
import matplotlib.pyplot as plt

"""
Funções para gerar e visualizar grafos a partir de dados de embarque e destino.
"""
def plotar_grafo_scale_free(G, dados):
    plt.figure(figsize=(16, 12))  
    
    sobrenomes = set(d['sobrenome_limpo'] for d in dados)
    portos = set(d['porto_embarque'] for d in dados)
    destinos = set(d['destino'] for d in dados)
    
    cores_portos = {
        'liverpool': '#8B0000', 'são francisco': '#FF4500',
        'londres': '#FFD700', 'porto': '#000080',
        'new jersey': '#8B4513', 'west prensten': '#800080',
        'tenerife': '#FFA07A', 'southampton': '#228B22',
        'leixões': '#ff5733'
    }
    
    node_colors = []
    for node in G.nodes:
        if node in sobrenomes:
            node_colors.append('lightblue')
        elif node in portos:
            node_lower = node.lower().strip()
            node_colors.append(cores_portos.get(node_lower, 'lightpink'))
        else:
            node_colors.append('yellow')
    
    edge_colors = []
    for u, v in G.edges():
        if u in portos:
            porto_lower = u.lower().strip()
            edge_color = cores_portos.get(porto_lower, 'lightpink')
            edge_colors.append(edge_color)
        else:
            edge_colors.append('#808080')
    
    node_sizes = []
    for node in G.nodes:
        if node in sobrenomes:
            node_sizes.append(500)
        elif node in portos:
            node_sizes.append(5000)
        else:
            node_sizes.append(20000)
    
    pos = nx.spring_layout(G, seed=42, k=0.5)
    nx.draw(
        G,
        pos,
        with_labels=True,
        node_color=node_colors,
        edge_color=edge_colors,
        node_size=node_sizes,
        font_size=8,
        font_weight='bold',
        arrowsize=20,
        alpha=0.9
    )
    
    plt.gca().set_axis_off()
    plt.title("Grafo de Embarque: Origens → Destinos", fontsize=14)
    plt.subplots_adjust(left=0.05, right=0.95, top=0.95, bottom=0.05)  
    plt.show()

def plotar_grafo_small_world(G, dados):
    plt.figure(figsize=(16, 12))
    procedencias = set(d['Procedencia'] for d in dados)
    portos = set(d['Porto de Embarque'] for d in dados)

    cores_portos = {
        'liverpool': '#8B0000', 'são francisco': '#FF4500',
        'porto': '#000080', 'west prensten': '#800080',
        'tenerife': '#FFA07A', 'southampton': '#228B22',
        'leixões': '#ff5733'
    }
    cor_padrao_porto = 'lightpink'
    cor_procedencia = 'lightblue'

    node_colors = []
    node_sizes = []
    for node in G.nodes:
        if node in procedencias:
            node_colors.append(cor_procedencia)
            node_sizes.append(500)
        else:
            node_lower = node.lower().strip()
            node_colors.append(cores_portos.get(node_lower, cor_padrao_porto))
            node_sizes.append(5000)

    pos = nx.spring_layout(G, seed=42, k=0.5)
    nx.draw(
        G,
        pos,
        with_labels=True,
        node_color=node_colors,
        node_size=node_sizes,
        font_size=8,
        alpha=0.9
    )

    edge_labels = {(u, v): d['data_chegada'] for u, v, d in G.edges(data=True)}
    nx.draw_networkx_edge_labels(
        G,
        pos,
        edge_labels=edge_labels,
        font_size=6,
        alpha=0.7
    )

    plt.title("Grafo Small World: Procedência → Porto de Embarque (com Data de Chegada)", fontsize=14)
    plt.subplots_adjust(left=0.05, right=0.95, top=0.95, bottom=0.05) 
    plt.show()

def plotar_grafo_movimento_portos(G, dados):
    plt.figure(figsize=(16, 12))

    sobrenomes = set(d['sobrenome_limpo'] for d in dados)
    portos = set(d['porto_embarque'] for d in dados)
    destinos = set(d['destino'] for d in dados)

    cores_portos = {
        'liverpool': '#8B0000', 'são francisco': '#FF4500',
        'londres': '#FFD700', 'porto': '#000080',
        'new jersey': '#8B4513', 'west prensten': '#800080',
        'tenerife': '#FFA07A', 'southampton': '#228B22',
        'leixões': '#ff5733'
    }

    node_colors = []
    for node in G.nodes:
        if node in sobrenomes:
            node_colors.append('lightblue')
        elif node in portos:
            node_lower = node.lower().strip()
            node_colors.append(cores_portos.get(node_lower, 'lightpink'))
        else:
            node_colors.append('yellow')

    edge_colors = []
    for u, v in G.edges():
        if u in portos:
            porto_lower = u.lower().strip()
            cor = cores_portos.get(porto_lower, 'lightpink')
        else:
            cor = '#808080'  
        edge_colors.append(cor)

    node_sizes = []
    for node in G.nodes:
        if node in sobrenomes:
            node_sizes.append(500)
        elif node in portos:
            node_sizes.append(5000)
        else:
            node_sizes.append(20000)

    pos = nx.spring_layout(G, seed=42, k=0.5)
    nx.draw(
        G,
        pos,
        with_labels=True,
        node_color=node_colors,
        edge_color=edge_colors,
        node_size=node_sizes,
        font_size=8,
        font_weight='bold',
        arrows=True,
        arrowsize=20,
        alpha=0.9
    )

    plt.gca().set_axis_off()
    plt.title("Grafo Bipartido Direcionado: Porto → Pessoa → Destino", fontsize=14)
    plt.subplots_adjust(left=0.05, right=0.95, top=0.95, bottom=0.05)
    plt.show()

def plotar_grafo_familia_para_europa(G, dados):
    plt.figure(figsize=(16, 12))  
    
    sobrenomes = set(d['sobrenome_limpo'] for d in dados)
    portos = set(d['porto_embarque'] for d in dados)

    cores_portos = {
        'liverpool': '#8B0000', 'são francisco': '#FF4500',
        'londres': '#FFD700', 'porto': '#000080',
        'new jersey': '#8B4513', 'west prensten': '#800080',
        'tenerife': '#FFA07A', 'southampton': '#228B22',
        'leixões': '#ff5733'
    }

    node_colors = []
    node_sizes = []
    for node in G.nodes:
        if node in sobrenomes:
            node_colors.append('lightblue')
            node_sizes.append(500)
        elif node in portos:
            node_lower = node.lower().strip()
            node_colors.append(cores_portos.get(node_lower, 'lightpink'))
            node_sizes.append(5000)
        else:
            node_colors.append('yellow')
            node_sizes.append(20000)

    edge_colors = []
    for u, v in G.edges():
        if v in portos:
            porto_lower = v.lower().strip()
            edge_color = cores_portos.get(porto_lower, 'lightpink')
            edge_colors.append(edge_color)
        else:
            edge_colors.append('#808080')

    pos = nx.spring_layout(G, seed=42, k=0.5)
    nx.draw(
        G,
        pos,
        with_labels=True,
        node_color=node_colors,
        edge_color=edge_colors,
        node_size=node_sizes,
        font_size=8,
        font_weight='bold',
        arrowsize=20,
        alpha=0.9
    )

    plt.gca().set_axis_off()
    plt.title("Grafo Família → Porto Europeu", fontsize=14)
    plt.subplots_adjust(left=0.05, right=0.95, top=0.95, bottom=0.05)
    plt.show()

def plotar_grafo_europa_para_brasil(G, dados, grafo_familia_europa):
    plt.figure(figsize=(16, 12))  
    
    portos = set(d['porto_embarque'] for d in dados)
    destinos = set(d['destino'] for d in dados)

    cores_portos = {
        'liverpool': '#8B0000', 'são francisco': '#FF4500',
        'londres': '#FFD700', 'porto': '#000080',
        'new jersey': '#8B4513', 'west prensten': '#800080',
        'tenerife': '#FFA07A', 'southampton': '#228B22',
        'leixões': '#ff5733'
    }
    centralidade = nx.degree_centrality(grafo_familia_europa)

    node_colors = []
    node_sizes = []
    for node in G.nodes:
        if node in portos:
            node_lower = node.lower().strip()
            node_colors.append(cores_portos.get(node_lower, 'lightpink'))
            node_sizes.append(5000 + centralidade.get(node, 0) * 10000)
        elif node in destinos:
            node_colors.append('#90EE90')
            node_sizes.append(20000)
        else:
            node_colors.append('yellow')
            node_sizes.append(500)

    edge_colors = []
    for u, v in G.edges():
        if u in portos:
            porto_lower = u.lower().strip()
            edge_color = cores_portos.get(porto_lower, 'lightpink')
            edge_colors.append(edge_color)
        else:
            edge_colors.append('#808080')

    pos = nx.spring_layout(G, seed=42, k=0.5)
    nx.draw(
        G,
        pos,
        with_labels=True,
        node_color=node_colors,
        edge_color=edge_colors,
        node_size=node_sizes,
        font_size=8,
        font_weight='bold',
        arrowsize=20,
        alpha=0.9
    )

    plt.gca().set_axis_off()
    plt.title("Grafo Porto Europeu → Brasil (Escalado pela centralidade anterior)", fontsize=14)
    plt.subplots_adjust(left=0.05, right=0.95, top=0.95, bottom=0.05)
    plt.show()