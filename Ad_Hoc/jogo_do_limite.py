def jogo_do_limite():
    """
    Alice e Bob decidiram jogar um jogo simples para passar o tempo.
    Este jogo é jogado com um baralho contendo N cartas, numeradas
    de 1 a N. Uma carta está inicialmente na mesa. Além disso, há
    uma pilha contendo todas as outras cartas do baralho.

    Alice começa retirando uma carta do topo da pilha. Ela então verifica
    se a diferença absoluta entre a carta que está atualmente na mesa e
    a carta retirada da pilha é no máximo um limite L. Em outras palavras,
    se a carta atualmente na mesa for T e a carta retirada da pilha for S,
    então ela verifica se |T-S| ≤ L. Se isto for verdade, ela substitui a
    carta na mesa pela carta removida, e marca |T-S| pontos. Se isto não
    for verdade, ela não faz nada -- a carta na mesa não é alterada, e ela
    não marca nenhum ponto.

    Bob então joga fazendo a mesma coisa. Ele remove uma carta da pilha, a
    compara com a carta atualmente na mesa e age de acordo. Alice então joga
    novamente, seguida de Bob, seguido novamente de Alice, e assim por diante.
    Eles continuam jogando até que a pilha de cartas esteja vazia. Sua tarefa
    é determinar a pontuação final de ambos os jogadores.

    Entrada
    A primeira linha contém três inteiros N, T0 e L (1 ≤ N < 60, N é impar, 1 ≤ T0
    ≤ N, 1 ≤ L ≤ 10), o número de cartas, a carta inicialmente na mesa, e o limite
    L. As próximas N-1 linhas contém um inteiro Si cada (1 ≤ Si ≤ N). Estes inteiros
    descrevem as cartas na pilha, em ordem. A primeira carta dada na entrada é a
    carta no topo da pilha. Todas as cartas usadas no jogo são distintas.

    Saída
    Imprima uma linha com dois inteiros A e B separados por um espaço, onde A é a
    pontuação final de Alice, e B é a pontuação final de Bob.
    :return:
    """
    entrada = list(map(int, input().strip().split(" ")))
    n, t, l = entrada[0], entrada[1], entrada[2]
    alice, bob, flag, = 0, 0, 0
    for i in range(n - 1):
        carta = int(input())
        diff = abs(t - carta)
        if diff <= l and i % 2 == 0:
            alice += diff
            t = carta
        if diff <= l and i % 2 == 1:
            bob += diff
            t = carta
    print(alice, bob)


jogo_do_limite()
