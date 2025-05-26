from math import sqrt


def uri():
    """
    Uilton, Rita e Ingred criaram um novo jogo para decidir
    quem não pagará sua parte da pizza do próximo final de
    semana e deram o nome de "URI" para o jogo (talvez eles
    decidiram unir as iniciais de seus nomes para formar o nome
    do jogo). O URI consiste de N rodadas, a cada rodada, cada
    um dos três jogadores falam um número, não é permitido números
    iguais em uma rodada. Se o número que o jogador falar for uma
    potência de 2, o mesmo ganha 1 ponto, e se além de ser uma potência
    de 2, for o maior número da rodada, o jogador ganha mais 1 ponto,
    se o número não for potência de 2 o jogador não ganha nenhum ponto.
    Sua tarefa é criar um programa que os ajude a contabilizar a pontuação
    e informar o vencedor, dado a quantidade de rodadas, e os números
    de cada rodada.

    Considere que as 4 primeiras potências de 2 são: 2, 4, 8, 16.

    Entrada
    A entrada contém vários casos de teste. A primeira linha de entrada contém
    um único inteiro N indicando o número de rodadas (1 ≤ 10⁵), cada uma das N
    linhas seguintes contem 3 números inteiros Ui, Ri, Ii (1 < Ui, Ri, Ii ≤ 10⁹),
    representando respectivamente o número de Uilton, Rita e Ingred na i-ésima
    rodada. O final da entrada é indicado quando N = 0.

    Saída
    Para cada caso de teste imprima uma única linha contendo o nome do jogador que
    tenha a maior quantidade de pontos. Caso haja empate no primeiro lugar, imprima
    o nome do jogo "URI" (sem aspas).
    :return:
    """
    n = int(input())
    while n != 0:
        u, r, i = 0, 0, 0
        for j in range(n):
            rodada = list(map(int, input().strip().split(" ")))
            if sqrt(rodada[0]) % 2 == 0 or sqrt(rodada[0]) % sqrt(2) == 0 :
                u += 1
                if max(rodada) == rodada[0]:
                    u += 1
            if sqrt(rodada[1]) % 2 == 0 or sqrt(rodada[1]) % sqrt(2) == 0:
                r += 1
                if max(rodada) == rodada[1]:
                    r += 1
            if sqrt(rodada[2]) % 2 == 0 or sqrt(rodada[2]) % sqrt(2) == 0:
                i += 1
                if max(rodada) == rodada[2]:
                    i += 1
        if u > r and u > i:
            print("Uilton")
        elif r > u and r > i:
            print("Rita")
        elif i > u and i > r:
            print("Ingred")
        else:
            print("URI")
        n = int(input())


uri()
