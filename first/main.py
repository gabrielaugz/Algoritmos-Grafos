from graph import grafo_simples, grafo_direcionado, grafo_barabasi_albert, grafo_random, grafo_small_world
from metrics import calcular_metricas, metricas_globais, propriedades_estruturais
from view import mostrar_grafo, plotar_distribuicao_de_grau, mostrar_centro

# Função geral para executar a análise de um grafo
def executar_analise(grafo, nome, plotar_grau=False):
    print(f"\n=== {nome} ===")
    
    mostrar_grafo(grafo, nome)
    
    print("\nMétricas locais:")
    print(calcular_metricas(grafo))

    print("\nMétricas globais:")
    print(metricas_globais(grafo))

    print("\nPropriedades estruturais:")
    print(propriedades_estruturais(grafo))

    mostrar_centro(grafo, f"Centro - {nome}")

    if plotar_grau:
        plotar_distribuicao_de_grau(grafo, f"Distribuição de Grau - {nome}")

G1 = grafo_simples()
G2 = grafo_direcionado()
G3 = grafo_barabasi_albert()
G4 = grafo_random()
G5 = grafo_small_world()

# Execução das análises
executar_analise(G1, "Grafo Simples")
executar_analise(G2, "Grafo Direcionado")
executar_analise(G3, "Grafo Barabási-Albert", plotar_grau=True)
executar_analise(G4, "Grafo Erdős–Rényi (Random)", plotar_grau=True)
executar_analise(G5, "Grafo Watts–Strogatz (Small-world)")