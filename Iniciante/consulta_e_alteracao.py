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
    n, q = map(int, input().split(" "))
    v = list(map(int, input().split(" ")))
    for i in range(q):
        soma, somas, mdc = 0, [], 0
        dados = list(map(int, input().split(" ")))
        while len(dados) != 3:
            dados = list(map(int, input().split(" ")))
        if dados[0] == dados[1]:
            soma = dados[0] + dados[2]
            mdc = gcd(v[dados[0] - 1], v[dados[0] - 1])
        for k in range(dados[0] - 1, dados[1]):
            soma += v[k] + dados[2]
            somas.append(soma)
            if len(somas) >= 2:
                mdc = gcd(somas[0], somas[1])
                somas = []
        print(mdc)


consulta_e_alteracao()
