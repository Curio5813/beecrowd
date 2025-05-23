from math import ceil, floor
from copy import deepcopy
from traceback import print_tb


def outra_crise():
    """
    Há dois anos atrás, uma nova crise mundial teve início, deixando muitas
    pessoas com problemas econômicos. Alguns trabalhadores de uma empresa
    estão tentando pedir um aumento de salário.

    A empresa possui uma hierarquia restrita, onde cada empregado tem exatamente
    um chefe, com a exceção do dono da companhia que não tem chefe. Empregados que
    não são chefes de nenhum outro empregado são chamados trabalhadores. O resto
    dos empregados e o dono são chamados de chefes.

    Para pedir aumento, um trabalhador deve enviar uma petição ao seu chefe direto.
    Evidentemente, cada chefe é encorajado a tentar manter seus subordinados felizes
    com seu salário atual, tornando o lucro da empresa o maior possível. No entanto,
    quando ao menos T porcento de seus subordinados diretos fazem uma petição, o chefe
    será pressionado e não terá escolha a não ser enviar uma petição ele mesmo ao seu
    superior direto. Cada chefe envia no máximo uma petição para seu próprio chefe,
    independente do seu número de subordinatos que o enviaram. Um chefe somente considera
    seus subordinados diretos (os que fizeram a petição e os que não a fizeram) para
    calcular o a porcentagem da pressão.

    Note que um chefe pode ter trabalhadores e chefes como seus subordinados diretos ao
    mesmo tempo, e ele pode receber petições de ambos os tipos de empregados. Cada subordinado
    direto, independente de seu cargo, terá peso 1 ao realizar o balanço total. Quando uma
    petição chega ao dono da empresa, todos os salários são aumentados. O sindicato dos
    trabalhadores está desesperado tentando fazer isso acontecer, então eles precisam convencer
    alguns trabalhadores a enviar uma petição aos seus chefes.

    Dados a hierarquia da empresa e o parâmetro T, você deve encontrar o menor número de
    trabalhadores que deve enviar uma petição de forma a fazer com que o dono da empresa
    aumente os salários.

    Entrada
    A entrada contém vários casos de teste. Cada caso de teste é dado em exatamente duas
    linhas. A primeira linha contém dois inteiros N e T (1 ≤ N ≤ 105 e 1 ≤ T ≤ 100), separados
    por um espaço em branco. N indica o número de empregados da empresa (sem considerar o dono)
    e T é o parâmetro descrito acima. Cada um dos empregados é identificado por um inteiro entre
    1 e N, inclusive. O dono é identificado pelo número 0. A segunda linha contém uma lista de
    inteiros separados por um espaço em branco. O inteiro Bi, na posição i dessa lista (começando
    de 1), indica o identificador do chefe direto do empregado i (0 ≤ Bi ≤ i - 1).

    O último caso de teste é seguido de uma linha contendo dois zeros separados por um espaço em
    branco.

    Saída
    Para cada caso de teste, imprima uma única linha contendo um único inteiro, a menor quantidade
    de trabalhadores que deve enviar uma petição de modo a fazer com que o dono da empresa receba
    uma petição.
    :return:
    """
    entrada = list(map(int, input().strip().split(" ")))
    n, t = entrada[0], entrada[1]
    while n != 0 and t != 0:
        workers = list(map(int, input().strip().split(" ")))
        temp, worker, chief = [], 0, 0
        for i in range(0, len(workers)):
            workers[i] += 1
        if workers.count(workers[0]) == len(workers):
            quorum = round(len(workers) * (t/100))
            print(quorum)
        else:
            for i in range(0, len(workers)):
                if i + 1 not in workers:
                    # print(i + 1, end=" ")
                    worker += 1
                    if i < len(workers) - 1 and workers[i] not in temp:
                        temp.append(workers[i])
            chief = n - worker - len(temp)
            peticoes = chief
            quorum = ceil(peticoes * (t/100))
            # print(temp, chief)
            print(quorum)
        entrada = list(map(int, input().strip().split(" ")))
        n, t = entrada[0], entrada[1]


outra_crise()


"""
3 100
0 0 0
3 50
0 0 0
14 60
0 0 1 1 2 2 2 5 7 5 7 5 7 5
1 73
0
4 50
0 0 1 1
3 86
0 1 1
13 85
0 0 0 0 0 3 3 4 2 4 5 4 1
1 89
0
11 86
0 0 0 2 1 0 0 0 4 6 5
13 90
0 0 2 2 3 1 2 4 0 5 7 2 9
13 90
0 0 0 0 1 2 0 2 4 5 5 3 2
13 45
0 0 1 1 2 2 3 3 4 4 5 5 6
7 68
0 0 1 1 2 2 3
1 81
0
0 0
"""