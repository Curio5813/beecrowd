def poker_do_rei():
    """
    Poker é um dos jogos de cartas mais jogados, e o Poker do Rei é
    uma das suas variações. O jogo é jogado com um baralho normal de
    52 cartas. Cada carta tem um dos quatro naipes e uma das 13 categorias.
    Entretanto, no Poker do Rei os naipes das cartas não são relevantes,
    enquanto as categorias são Ás (categoria 1), 2, 3, 4, 5, 6, 7, 8, 9, 10,
    Valete (categoria 11), Rainha (categoria 12) e Rei (categoria 13). O nome
    do jogo vem do fato de que no Poker do Rei, o Rei é a carta com a
    categoria mais alta. Mas esta não é a única diferença entre o Poker regular
    e o Poker do Rei. Aos jogadores do Poker do Rei são distribuídos uma mão
    de apenas três cartas. Existem três tipos de mãos:

    Um set, feito de três cartas da mesma categoria.
    Um par, que contém duas cartas da mesma categoria, com a outra carta sem
    correspondente.
    Um não-par, onde não tem-se duas cartas da mesma categoria.
    As mão são classificadas usando as seguintes regras:

    Qualquer set derrota qualquer par e não-par.
    Qualquer par derrota qualquer não-par.
    Um set formado com cartas de categoria maior derrota qualquer set formado com
    cartas de categoria menor.
    Se as cartas emparelhadas de dois pares têm categorias diferentes, então o par
    com as cartas emparelhadas de maior categoria derrota o par com as cartas emparelhadas
    de menor categoria.
    Se as cartas emparelhadas de dois pares têm a mesma categoria, então a cartas não
    emparelhadas de ambos os pares são comparadas; o par com carta não emparelhada de
    maior categoria derrota o par com carta não emparelhada de menor categoria, a menos
    que ambas as cartas não emparelhadas sejam da mesma categoria, caso no qual temos um
    empate.
    Uma nova empresa de software quer oferecer jogos de Poker do Rei no seu site de jogos,
    e precisa de um software que, dada uma mão de Poker do Rei, determine o set ou o par
    com menor categoria que derrota a mão dada. Você pode codificá-lo?

    Entrada
    Cada caso de teste é descrito usando uma única linha. A linha contém três inteiros A, B
    e C representando as categorias das cartas entregues na mão (1 ≤ A, B, C ≤ 13).

    O último caso de teste é seguido por uma linha contendo três zeros.

    Saída
    Para cada caso de teste imprima uma única linha. Se existe um set ou um par que derrota
    a mão dada, escreva a menor mão que o faz. A mão vencedora deve ser escrita especificando
    as categorias de suas cartas, em ordem não-descrescente. Se nenhum set ou par derrota a
    mão dada, escreva o caractere '*' (asterisco).
    :return:
    """
    mao = list(map(int, input().strip().split(" ")))
    while mao.count(0) != 3:
        mao.sort()
        if mao.count(mao[0]) == 3 and mao[0] == 13:
            print("*")
        elif mao[0] != mao[1] and mao[1] != mao[2] and mao[2] != mao[0]:
            print(1, 1, 2)
        elif mao.count(mao[0]) == 3:
            print(mao[0] + 1, mao[0] + 1, mao[0] + 1)
        elif mao.count(mao[0]) == 2 and mao[2] == 13:
            print(1, mao[1] + 1, mao[1] + 1)
        elif mao.count(mao[0]) == 2 and mao[2] != 13:
            print(mao[0], mao[0], mao[2] + 1)
        elif mao.count(mao[0]) == 1 and mao[0] == 12 and mao[1] == 13:
            print(1, 1, 1)
        elif mao.count(mao[0]) == 1 and mao[0] < 12 and mao[1] == 13:
            print(mao[0] + 1, mao[1], mao[1])
        elif mao.count(mao[0]) == 1 and mao[1] != 13 and mao[1] - mao[0] == 1:
            print(mao[1], mao[1], mao[1] + 1)
        elif mao.count(mao[0]) == 1 and mao[1] != 13 and mao[1] - mao[0] > 1:
            print(mao[0] + 1, mao[1], mao[1])
        mao = list(map(int, input().strip().split(" ")))


poker_do_rei()
