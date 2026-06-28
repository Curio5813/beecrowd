from math import gcd


def consulta_e_alteracao():
    """
    Dado um vetor com N elementos responda Q queries dos tipos:
    1 A B V: Somar V em todos os elementos da posição A até a posição B do vetor.
    2 A B: Retorna o Máximo Divisor Comum de todos os elementos das posições A
    até B no vetor
    A entrada consiste em diversos casos de teste. A primeira linha de cada caso
    de teste contém dois inteiros N Q, representando respectivamente o tamanho do
    vetor e a quantidade de queries. A segunda linha da entrada contém N inteiros
    representando os elementos do vetor. As próximas Q linhas contém as queries como
    descrito anteriormente. Os limites: 1 ≤ N; Q ≤ 105. A saída para cada query do
    tipo dois imprima o MDC de todas as posições do vetor que estão no intervalo AB
    :return:
    """
    while True:
        try:
            entrada1 = input().strip().split(" ")
            n, q = int(entrada1[0]), int(entrada1[1])
            entrada2 = input().strip().split(" ")
            v = []
            for i in range(0, len(entrada2)):
                v.append(int(entrada2[i]))
            for i in range(q):
                mdc, dados, flag = 0, [], 0
                entrada3 = input().strip().split(" ")
                for j in range(0, len(entrada3)):
                    dados.append(int(entrada3[j]))
                for j in range(0, len(dados)):
                    if dados[0] == 1:
                        for p in range(dados[1] - 1, dados[2]):
                            v[p] += dados[3]
                        # print(v)
                        break
                    if dados[0] == 2:
                        # print(v)
                        res = gcd(v[dados[1] - 1], v[dados[1]])
                        for p in range(dados[1], dados[2]):
                            mdc = gcd(res, v[p])
                            res = mdc
                        print(mdc)
                        break
        except EOFError:
            break


consulta_e_alteracao()

