# ALGORITMO DE APROXIMAÇÃO, DESCOBRIR AS MELHORES ESTAÇÕES PARA ABRANGER A MAIOR PARTE DOS ESTADOS DO PAIS COM MENOR CUSTO.
# LISTA DE ESTADOS
estados_abranger = set(["mt", "wa", "or", "id", "nv", "ut", "ca", "az"])
# LISTA DE ESTAÇÕES
estacoes = {}
estacoes["kum"] = set(["id", "nv", "ut"])
estacoes["kdois"] = set(["wa", "id", "mt"])
estacoes["ktres"] = set(["or", "nv", "ca"])
estacoes["kquatro"] = set(["nv", "ut"])
estacoes["kcinco"] = set(["ca", "az"])
estacoes_finais = set()

while estados_abranger:
    melhor_estacao = None
    estados_cobertos = set()
    for estacao, estados_por_estacao in estacoes.items():
        cobertos = estados_abranger & estados_por_estacao
        if len(cobertos) > len(estados_cobertos):
            melhor_estacao = estacao
            estados_cobertos = cobertos

    estados_abranger -= estados_cobertos
    estacoes_finais.add(melhor_estacao)
    
print(estacoes_finais)




# O QUE PODEMOS FAZER COM CONJUNTOS
frutas = set(["abacate", "tomate", "banana"])
vegetais = set(["beterraba", "cenoura", "tomate"])
frutas | vegetais # ISSO É UMA UNIÃO
frutas & vegetais # ISSO É UMA INTERSEÇÃO
frutas - vegetais # ISSO É UMA DIFERENÇA
