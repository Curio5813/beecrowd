def jogo_da_velha():
    """
    O jogo da velha é um dos jogos mais antigos da humanidade; os
    primeiros registros dele são do século I antes de Cristo, no
    Império Romano. João e Maria jogam bastante jogo da velha, mas
    depois de algum tempo eles decidiram jogar uma variante do jogo
    da velha tradicional, o jogo da velha 1-D.

    O jogo da velha 1-D é um jogo disputado por dois jogadores em um
    tabuleiro 1 × N; inicialmente, todas as casas do tabuleiro estão
    vazias. Os jogadores alternam-se desenhando uma cruz sobre uma casa
    vazia. O primeiro jogador a completar uma sequência de três ou mais
    cruzes em casas consecutivas ganha o jogo.

    Maria logo percebeu que, dependendo da situação do jogo, sendo sua
    vez de jogar, ela pode sempre garantir a vitória, independente das
    jogadas de João. Isto é relativamente fácil para tabuleiros menores,
    mas para tabuleiros maiores, mesmo após várias jogadas, esta tarefa é
    mais difícil; por isso, ela pediu que você escrevesse um programa que,
    dada a situação do tabuleiro, decide se ela tem uma estratégia vencedora.

    Entrada
    A entrada contém vários casos de teste. A primeira linha de caso de teste
    contém um inteiro N, indicando o tamanho do tabuleiro (3 ≤ N ≤ 104).
    A linha seguinte contém uma sequência de N caracteres indicando quais
    casas do tabuleiro já foram ocupadas: um ‘.’ indica que a casa correspondente
    está vazia, enquanto um ‘X’ indica que a casa já teve uma cruz desenhada
    sobre ela. A entrada nunca contém três ‘X’ consecutivos.

    O ultimo caso de teste é seguido por uma linha que contém um único número zero.

    Saída
    Para cada caso de teste da entrada seu programa deve imprimir uma única linha
    contendo um único caractere: ‘S’ caso Maria possua uma estratégia vencedora e
    ‘N’ caso contrário.
    :return:
    """
    n = int(input())
    while n != 0:
        str_velha = input()
        div_x = str_velha.split("X")
        print(div_x)
        print(div_x)
        cont = str_velha.count("X")
        if (n - cont) % 2 != 0:
            print("S")
        elif (n - cont) % 2 == 0:
            print("N")
        n = int(input())


jogo_da_velha()
