from statistics import mean
from math import sqrt


def porque_arte():
    """
    Leo é um designer. Ele tem uma coleção de N fontes e N cores, cada uma
    com uma nota inteira que indica o quão bonita ela é. Uma nota negativa
    indica que a fonte ou cor é "feia".

    Com base nisso, Leo inventou uma nova forma de medir a beleza de qualquer
    texto. Se um texto tiver uma fonte de nota Fi e uma cor de nota Cj, então
    a beleza do texto é o produto Fi × Cj. Note que quando tanto a fonte quanto
    a cor são feias, o texto resultante é bonito, porque, Arte!

    Leo tem que apresentar ao seu chefe k designs de texto bonitos. O chefe disse
    a ele que os textos devem ser realmente diferentes uns dos outros. Com isso
    em mente, Leo decidiu selecionar uma fonte distinta e uma cor distinta para
    cada texto, de tal forma que a soma das belezas dos k textos formados seja
    máxima. Para seu orgulho, ele também quer saber a soma mínima possível das
    belezas de k textos feitos com fontes e cores distintas.

    Mas há um problema! Leo esqueceu de quantos designs o chefe pediu, então ele
    precisa encontrar a resposta para cada inteiro k entre 1 e N.

    Entrada
    A primeira linha contém um inteiro N (1 ≤ N ≤ 105) indicando o número de fontes e
    cores. A segunda linha contém N inteiros F1, F2, ... , FN (−104 ≤ Fi ≤ 104 para
    i = 1, 2, ... , N), representando as notas das fontes. A terceira linha contém
    N inteiros C1, C2, ... , CN (−104 ≤ Ci ≤ 104 para i = 1, 2, ... , N), denotando
    as notas das cores.

    Saída
    Imprima N linhas, de modo que a k-ésima linha contenha dois inteiros indicando,
    respectivamente, a soma mínima e máxima das belezas se o chefe pedir k textos.
    :return:
    """
    n = int(input())
    fontes, cores = [], []
    for i in range(2):
        if i == 0:
            fontes = list(map(int, input().split()))
        if i == 1:
            cores = list(map(int, input().split()))
    possiveis_designers = []
    for i in range(1, n + 1):
        possiveis_designers.append(i)


porque_arte()

"""
4
0 -1 1 2
10 20 30 40
"""
