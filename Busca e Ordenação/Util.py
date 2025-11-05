# Este arquivo é um modulo, não executamos módulos, módulos só contêm funções

# Função para realizar a busca linear em uma lista númerica (linear pq aumenta de acordo com o vetor)
# A função deve receber como parâmetro a lista e o valor a ser localizado
def buscar(lista: list[int], valor: int) -> int:
    indice = 0
    
    for i in range(len(lista)):
        if lista[i] == valor:
            indice = lista[i]
            return i
        else:
            return -1

# Função para ordenar uma lista de números inteiros em ordem crescente (usando o método bolha)
def ordenar(lista: list[int]) -> list[int]:
    for _ in range(len(lista)):
        for i in range(len(lista) - 1): # Se for de 0 a 9, vai até o 8 e não estoura pois chega até o limite da lista (9)
            if lista[i] > lista[i + 1]:
                lista[i], lista[i + 1] = lista[i + 1], lista[i]
    return lista