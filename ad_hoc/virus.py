from math import floor


def virus():
    """
    A secretaria de saúde pública da Nlogônia acabou de emitir um alerta.
    Um vírus está contagiando toda a população.

    Após muitos estudos, os pesquisadores do país determinaram que, após
    infiltrarem o corpo hospedeiro, os virus se juntam dois a dois para
    tornarem-se letais. O nível de letalidade de uma infecção é determinado
    pela soma da diferença da idade, em dias, dos vírus pareados. Os vírus
    sem pares não influenciam no nível.

    Desta forma, se existem 4 vírus no corpo hospedeiro com idades (em dias),
    iguais a

    4, 10, 9, 43

    E eles se paream da seguinte forma:

    4 com 9, 43 com 10

    Então nível de letalidade seria (9 - 4) + (43 - 10) = 38.

    A secretaria de saúde pública da Nlogônia pediu para que você escrevesse
    um programa que, dado a contagem de vírus em um corpo e a idade de cada um deles,
    calcule o nível máximo de letalide que a infecção pode assumir.

    Entrada
    A entrada contém vários casos de teste. A primeira linha de cada caso contém um
    inteiro N (1 ≤ N ≤ 1000), a quantidade de vírus no corpo hospedeiro. A linha seguinte
    contém N números inteiros ai (0 ≤ ai ≤ 1000) separados por espaços, as idades
    (em dias) de todos os vírus no corpo.

    A entrada termina com fim-de-arquivo (EOF).

    Saída
    Para cada caso de teste, imprima uma única linha contendo o nível de letalidade
    máximo que a infecção pode assumir.
    :return:
    """
    while True:
        try:
            n = int(input())
            idades = list(map(int, input().split(" ")))
            idades.sort()
            letalidade = 0
            j = len(idades) - 1
            if len(idades) % 2 == 0:
                pares = len(idades) // 2
                for i in range(0, len(idades)):
                    if i == pares:
                        break
                    letalidade += idades[j] - idades[i]
                    j -= 1
            if len(idades) % 2 == 1:
                pares = floor(len(idades) / 2)
                for i in range(0, len(idades)):
                    if i == pares:
                        break
                    letalidade += idades[j] - idades[i]
                    j -= 1
            print(letalidade)
        except EOFError:
            break


virus()
