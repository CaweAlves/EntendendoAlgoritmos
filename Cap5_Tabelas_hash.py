
# PREÇOS DE ITENS EM UMA LOJA UTILIZANDO TABELAS HASH
caderno = dict()

caderno["maça"] = 0.67
caderno["leite"] = 2.49
caderno["abacate"] = 1.49

#print(caderno)
#print(caderno["abacate"])

# LISTA TELEFONICA UTILIZANDO TABELA HASH
lista_telefonica = {}
lista_telefonica["Eu"] = 13997634896
lista_telefonica["Kaio"] = 1199

#print(lista_telefonica["Eu"])

# LISTA DE CONFERENCIA DE VOTAÇÃO COM TABELA HASH
votaram = {}

def verifica_eleitor(nome):
    if votaram.get(nome):
        print ("Mande embora!")
    else:
        votaram[nome] = True
        print ("Deixa votar!")

verifica_eleitor("Tom")
verifica_eleitor("Tom")

# CACHE EM TABELAS HASH
# cache = {}

# def pega_pagina(url):
#     if cache.get(url):
#         return cache[url]
#     else:
#         dados = pega_dados_do_servidor(url)
#         cache[url] = dados
#         return dados