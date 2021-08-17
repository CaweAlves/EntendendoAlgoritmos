# # PRIMEIRA ABORDAGEM (NÂO RECURSIVA)

# def  procure_pela_chave(caixa_principal):
#     pilha = main_box.crie_uma_pilha_para_busca()
#     while pilha is not vazia:
#         caixa = pilha.pegue_caixa()
#         for item in caixa:
#             if item in caixa:
#                 if item.e_uma_caixa():
#                     pilha.append(item)
#                 elif item.e_uma_chave():
#                     print ("achei a chave!")


# ==========================================================================================  #


# SEGUNDA ABORDAGEM (RECURSIVA)

# def procure_pela_chave(caixa):
#     for item in caixa:
#         if item.e_uma_caixa():
#             procure_pela_chave(item)
#         elif item.e_uma_chave():    
#             print ("achei a chave!")


# ==========================================================================================  #


# CONTAGEM REGRESSIVA (RECURSIVA)

# def regressiva(i):
#     i = 5
#     print(i)
#     if i <= 1:
#         return
#     else:
#         regressiva(i-1)


# ==========================================================================================  #


# BOAS e TCHAU (RECURSIVO)

# def sauda(nome):
#     print("Olá, " + nome + "!")
#     sauda2(nome)
#     print ("preparando para dizer tchau...")
#     tchau()


# def sauda2(nome):
#     print("Como vai " + nome + "?")

# def tchau():
#     print("ok, tchau!")


# ==========================================================================================  #


#FATORAÇÂO (RECURSIVO)

# def fat(x):
#     if x == 1:
#         return 1
#     else:
#         return x * fat(x-1)