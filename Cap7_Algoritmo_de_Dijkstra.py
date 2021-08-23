# IMPLEMENTANDO O ALGORITMO DE DIJKSTRA

# O GRAFO
grafo = {}
grafo["inicio"] = {}
grafo["inicio"]["a"] = 6
grafo["inicio"]["b"] = 2

grafo["a"] = {}
grafo["a"]["fim"] = 1

grafo["b"] = {}
grafo["b"]["a"] = 3
grafo["b"]["fim"] = 5

grafo["fim"] = {}

# TABELA HASH PARA CUSTO DE CADA ARRESTA DO GRAFO
infinito = float("inf") # infinito
custos = {}
custos["a"] = 6
custos["b"] = 2
custos["fim"] = infinito

#TABELA HASH DE PAIS DO GRAFO
pais = {}
pais["a"] = "inicio"
pais["b"] = "inicio"
pais["fim"] = None

# ARRAY PARA MANTER O VÉRTECES JÁ PROCESSADOS
processados = []

# CODIGO DA IMPLEMENTAÇÃO
# FUNÇÃO PARA ENCONTRAR O VÉRTICE DE CUSTO MINIMO
def ache_no_custo_mais_baixo(custos):
    custo_mais_baixo = float("inf")
    nodo_custo_mais_baixo = None
    for nodo in custos:
        custo = custos[nodo]
        if custo< custo_mais_baixo and nodo not in processados:
            custo_mais_baixo = custo
            nodo_custo_mais_baixo = nodo
    return nodo_custo_mais_baixo
# LOGICA DO CODIGO: |
#                  V
# ENQUANTO HOUVER GRAFOS A SEREM PROCESSADOS |
#                                           V
# PEGUE O VÉRTECE QUE ESTÁ MAIS PRÓXIMO DO INÍCIO |
#                                                V
# ATUALIZE OS CUSTOS PARA OS SEUS VIINHOS |
#                                        V
# SE QUALQUER UM DOS CUSTOS DOS VIZINHOS FOR ATUALIZADO, ATUALIZE TAMBÉM O PAI |
#                                                                             V
# MARQUE O VÉRTECE COMO PROCESSADO (VOLTA AO INÍCIO DO LOOP).




nodo = ache_no_custo_mais_baixo(custos)
while nodo is not None:
    custo = custos[nodo]
    vizinhos = grafo[nodo]
    for n in vizinhos.keys():
        novo_custo = custo + vizinhos[n]
        if custos[n] > novo_custo:
            custos[n] = novo_custo
            pais[n] = nodo
    processados.append(nodo)
    nodo = ache_no_custo_mais_baixo(custos)
    print(nodo)

#print(grafo["inicio"].keys())
#print(grafo["inicio"]["a"])
#print(grafo["inicio"]["b"])




