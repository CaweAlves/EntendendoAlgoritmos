# Algoritmo de soma utilizando loop  
def soma(lista):
    total = 0
    for x in lista:
        total += x
    return total
    
print(soma([1, 2, 3, 4]))

# Algoritmo de soma utilizando a recursividade
def soma(lista):
    if lista == []:
        return 0
    return lista[0] + soma(lista[1:])

print(soma([1, 2, 3, 4]))
    
# Função recursiva que conta o número de itens em uma lista

def conta(lista):
    if lista == []:
        return 0
    return 1 + conta(lista[1:])

print(conta([1, 2, 3, 4, 23, 34]))

def maximo(lista):
    if len(lista) == 2:
        return lista[0] if lista[0] >  lista[1] else lista [1]
    sub_max = maximo(lista[1:])
    return lista [0] if lista[0] > sub_max else sub_max

print(maximo([1, 2, 3, 4, 23, 34]))

# Codigo para Quicksort
def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivo = array[0]
        menores = [i for i in array[1:] if i <= pivo]
        maiores = [i for i in array[1:] if i > pivo]
        return quicksort(menores) + [pivo] + quicksort(maiores)

print(quicksort([10, 5, 2, 3, -20, -1670]))