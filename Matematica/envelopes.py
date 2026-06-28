def envelopes():
    """
    Uma empresa quer mandar um envelope para obter uma resposta
    de um cliente e quer saber se é possível colocar esse envelope
    dentro de outro. Ambos envelopes são retangulares e um só pode
    ser colocado dentro do outro se as dimensões forem ambas menores.
    Dadas as dimensões dos dois envelopes, responda se é possível ou
    não colocar o primeiro dentro do segundo.

    Entrada
    A entrada consiste de uma série de testes. A primeira linha contém
    um único inteiro indicando o número n (1 ≤ n ≤ 20) de casos de testes.
    A seguir vêm n linhas contendo, cada uma, um caso de teste. Cada caso
    de teste se compõe de 4 inteiros: os dois primeiros são as dimensões
    do envelope que deve ir dentro e os dois últimos, a dimensão do envelope
    principal.

    Saída
    Para cada caso de teste imprima, em uma linha:

    . 'S' se for possível colocar o primeiro envelope dentro do segundo,

    ou

    . 'N', caso contrário.
    :return:
    """
    n = int(input())
    for i in range(n):
        envelopes1, envelopes2 = [], []
        d11, d12, d21, d22 = map(int, input().strip().split(" "))
        envelopes1.append(d11)
        envelopes1.append(d12)
        envelopes2.append(d21)
        envelopes2.append(d22)
        envelopes1.sort()
        envelopes2.sort()
        if envelopes1[0] >= envelopes2[0] or envelopes1[1] >= envelopes2[1]:
            print("N")
        else:
            print("S")


envelopes()
