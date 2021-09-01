# RESOLVENDO O PROBLEMA DA MOCHILA COM PROGRAMAÇÃO DINÂMICA (CADA CELULA DA TABELA É UM SUBPROBLEMA)

# TABELA DA PROGRAMAÇÃO DINAMICA PARA O PROBLEMA DA MOCHILA (ROUBAR ITEMS MAIS VALIOSOS QUE CABEM NA MOCHILA)
#                      0.5  |  1  |  1.5  |  2  |  2.5  |  3  |  3.5  |  4    # <------- PESSOS QUE AS MOCHILAS SUPORTAM  
#Violão(1KG, 1.5K)      0    1.5K    1.5K  1.5K   1.5K   1.5K   1.5K   1.5K
#Rádio(4KG, 3K)         0    1.5K    1.5K  1.5K   1.5K   1.5K   1.5K    3K    
#Notebook(3KG, 2K)      0    1.5K    1.5K  1.5K   1.5K    2K    1.5K    3K
#Joia(0.5KG, 1K)       1K    1.5K     2K   2.5K    3K     3K    3.5K    4.5K -----> RESULTADO (NOTBOOK, VIOLÃO E JOIA) 

# TABELA DA PROGRAMAÇÃO DINAMICA PARA O PROBLEMA DA MOCHILA (IR AO MAXIMO DE LUGARES POSSIVEIS EM UMA VIAJEM A LONDRES)
#                                           ¹/² |  1  |  1¹/²  |  2     #<---- Tempo Em Londes (maximo de 2 dias em Londres)
# Westminter(1/2 dia, Ranking 7)             7     7      7       7   
# Teatro The Globe(1/2 dia, Ranking 6)       7    13     13      13
# Galeria Nacional(1 dia, Ranking 9)         7    13     16      22
# Museu Britânico(2 dia, Ranking 9)          7    13     16      22
# Catedral de São Paulo(1/2 dia, Ranking 8)  8    15     21      24 ----> RESULTADO (ABADIA DE WESTMINTER, GALERIA NACIONAL E CATEDRAL DE SÃO PAULO)

# comparando strings para sugestões
# Formulando o algoritmo em pseudocodigo (maior substrings):
# if palavra_a[i] == palavra_b[j]:
#     celula[i][j] = celula[i-1][j-1] + 1
# else:
#     celula[i][j] = 0

# Formulando o algoritmo em pseudocodigo (maior sequencia de substrings):
# if palavra_a[i] == palavra_b[j]:
#     celula[i][j] = celula[i-1][j-1] + 1
# else:
#     celula[i][j] = max(celula[i-1][j], celula[i][j-1])


# TABELA DA PROGRAMAÇÃO DINAMICA PARA calcular a maior substrings comum entre blue  e clues.
#
#       C  |  L  |  U  |  E  |  S
# B     0     0     0     0     0 
# L     0     1     0     0     0
# U     0     2     0     0     0
# E     0     0     0     3     0  <-----(RESULTADO: (3) STRINGS SEMELHANTES)