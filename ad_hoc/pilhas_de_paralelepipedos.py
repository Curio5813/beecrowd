def pilhas_de_paralelepipedos():
    """
    Uma jardineiro tem um monte de pedaços de granito em forma de
    paralelepípedo e quer formar uma escultura empilhando dois desses
    blocos. Ele pode virar convenientemente os blocos, mas só pode
    empilhar os dois blocos se a face do bloco que vai ficar em baixo
    tiver ambas as dimensões maiores que as da face que será empilhada.
    Faça um programa para ajudá-lo nessa tarefa.

    Entrada
    A entrada consiste de uma série de testes. A primeira linha contém
    um único inteiro indicando o número n (1 ≤ n ≤ 20) de casos de testes.
    A seguir vêm n linhas contendo, cada uma, um caso de teste. Cada caso
    de teste se compõe de 6 inteiros: os três primeiros são as dimensões
    do primeiro bloco e, as três últimas, as dimensões do segundo bloco.

    Saída
    Para cada caso de teste imprima, em uma linha, um inteiro de 0 a 3, com
    o seguinte significado:

    0, se nenhum bloco pode ser empilhado sobre o outro.

    1, se apenas o primeiro bloco pode ser empilhado sobre o segundo.

    2, se apenas o segundo bloco pode ser empilhado sobre o primeiro.

    3, Se cada bloco pode ser convenientemente empilhado sobre o outro.
    :return:
    """
    n = int(input())
    for i in range(n):
        bloco1, bloco2, cont1, cont2, idx1, idx2 = [], [], 0, 0, [], []
        blocos = list(map(int, input().split(" ")))
        for j in range(0, len(blocos)):
            if j <= 2:
                bloco1.append(blocos[j])
            if j > 2:
                bloco2.append(blocos[j])
        bloco1.sort()
        bloco2.sort()
        for j in range(0, len(bloco1)):
            for k in range(0, len(bloco2)):
                if bloco1[j] > bloco2[k] and k not in idx2:
                    cont1 += 1
                    idx2.append(k)
                    break
        for j in range(0, len(bloco2)):
            for k in range(0, len(bloco1)):
                if bloco2[j] > bloco1[k] and k not in idx1:
                    cont2 += 1
                    idx1.append(k)
                    break
        if cont1 >= 2 and cont2 >= 2:
            print(3)
        elif cont1 >= 2 > cont2:
            print(2)
        elif cont1 < 2 <= cont2:
            print(1)
        elif cont1 < 2 and cont2 < 2:
            print(0)


pilhas_de_paralelepipedos()
