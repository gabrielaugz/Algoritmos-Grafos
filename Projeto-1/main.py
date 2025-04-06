import graph_generation as gg
import graph_visualization as gv
import metrics_calculation as mc
import os

"""
Esse código é responsável por gerar e visualizar grafos a partir de dados de embarque e procedência.
"""
def main():
    dirname = os.path.dirname(__file__)
    caminho_csv = os.path.join(dirname, 'base23.csv')
    
    dados_embarque = gg.processar_dados_embarque_destino(caminho_csv)
    G_scale_free = gg.gerar_grafo_scale_free(dados_embarque)
    gv.plotar_grafo_scale_free(G_scale_free, dados_embarque)
    metrics = mc.calcular_metricas(G_scale_free)
    mc.exibir_metricas(metrics)

    dados_procedencia = gg.processar_dados_procedencia(caminho_csv)
    G_small_world = gg.gerar_grafo_small_world(dados_procedencia)
    gv.plotar_grafo_small_world(G_small_world, dados_procedencia)

    G_movimento_portos = gg.gerar_grafo_movimento_portos(dados_embarque)
    gv.plotar_grafo_movimento_portos(G_movimento_portos, dados_embarque)
    metrics_bipartido = mc.calcular_metricas(G_movimento_portos)
    mc.exibir_metricas(metrics_bipartido)

    G_familia_europa = gg.gerar_grafo_familia_para_europa(dados_embarque)
    gv.plotar_grafo_familia_para_europa(G_familia_europa, dados_embarque)
    metrics_familia_europa = mc.calcular_metricas(G_familia_europa)
    mc.exibir_metricas(metrics_familia_europa)

    G_europa_brasil = gg.gerar_grafo_europa_para_brasil(dados_embarque)
    gv.plotar_grafo_europa_para_brasil(G_europa_brasil, dados_embarque, G_familia_europa)
    metrics_europa_brasil = mc.calcular_metricas(G_europa_brasil)
    mc.exibir_metricas(metrics_europa_brasil)

if __name__ == "__main__":
    main()