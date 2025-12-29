def dado():
    """
    Um simples jogo de tabuleiro que gerações de crianças
    jogaram consiste em um tabuleiro contendo uma trilha de
    quadrados e um conjunto de peças coloridas. No começo do
    jogo cada peça é atribuída a um jogador; todas as peças
    são inicialmente posicionadas antes do primeiro quadrado
    da trilha.

    O jogo procede em rodadas. A cada rodada, jogadores lançam
    um par de dados e movem suas peças um número de quadrados
    para frente igual ao resultado rolado. Os jogadores jogam
    os dados sempre na mesma ordem (jogador A, depois jogador B,
    etc.) em cada rodada.

    Maioria dos quadrados no tabuleiro são quadrados planos (ou
    quadrados vazios), mas alguns são “armadilhas”. Se a peça de
    um jogador cair em um quadrado armadilha no fim de seu movimento,
    o jogador perde sua próxima jogada. Ou seja ele/ela não pode
    jogar os dados, e seu/sua peça fica uma rodada sem se movimentar.

    Haverá exatamente três armadilhas na trilha:

    O vencedor do jogo é o jogador que sua peça chega no fim da trilha primeiro.
    O fim da trilha é depois do último quadrado do tabuleiro. Considere, por exemplo,
    o tabuleiro da imagem acima, que tem quadrados numerados de 1 à 48. No começo,
    as peças são posicionadas no local marcado “Begin (início)” na figura, ou seja,
    antes do quadrado de número 1. Portanto, se um jogador rola um 7 (dados mostrando
    2 e 5 por exemplo) seu/sua peça estará posicionada no quadrado de número 7 no
    fim da primeira rodada do jogo. Além disso, se a peça de um jogador está
    posicionada no quadrado de número 41, o jogador precisa de um resultado de no
    mínimo 8 para chegar ao fim da trilha e ganhar o jogo. Note também que não haverá
    empate no jogo.

    Será dado a você um número de jogadores, o número de quadrados na trilha, o local
    das armadilhas e uma lista de resultados jogados nos dados. Você deve escrever um
    programa que determina o ganhador.

    Entrada
    Seu programa deve processar vários casos de teste. A primeira linha de um teste
    contém dois inteiros P e S representando respectivamente o número de jogadores e
    o número de quadrados na trilha (1 <= P <= 10 e 3 <= S <= 10000). A segunda linha
    descreve as armadilhas, representadas por três inteiros diferentes T1, T2 e T3,
    mostrando suas posições na trilha (1 <= T1, T2, T3 <= S). A terceira linha contém
    um único inteiro N indicando o número de rolagem de dados no teste. Cada uma das
    N linhas seguintes contém dois inteiros D1 e D2 (1 <= D1, D2, <= 6), representando
    os resultados da rolagem dos dados. O fim da entrada é indicado por P = S = 0. O
    conjunto de rolagem dos dados em um teste será sempre um número exato necessário
    para que um jogador ganhe o jogo.

    Um jogador é identificado por um número de 1 até P. Os jogadores jogam em uma rodada
    de uma forma sequencial de 1 para P.

    A entrada deve ser lida de uma forma padrão.

    Saída
    Para cada teste em sua entrada, seu programa deve apresentar um único inteiro: o
    número representando o jogador.

    A saída deve ser escrita de uma forma padrão.
    :return:
    """
    while True:
        p, s = map(int, input().strip().split(" "))
        jogador = {}
        for i in range(1, p + 1):
            jogador[i] = 0
        # print(jogador)
        if p == 0 and s == 0:
            break
        aramadilhas = list(map(int, input().strip().split(" ")))
        rodadas = int(input())
        chaves, cont, par, preso, temp, flag = 1, 0, rodadas, [], [], False
        while rodadas > 0:
            dados = sum(list(map(int, input().strip().split())))
            print(jogador, dados, chaves, preso, temp, cont, flag)
            if jogador[chaves] + dados in aramadilhas and chaves not in preso:
                preso.append(chaves)
                temp.append(dados)
            if chaves in preso and cont < par and flag == False:
                cont += p
                if cont >= par:
                    cont = 0
                    chaves += 1
                    if chaves > len(jogador):
                        chaves = 1
                        flag = True
            if flag:
                jogador[chaves] += temp[preso.index(chaves)]
                temp.remove(temp[preso.index(chaves)])
                preso.remove(chaves)
                chaves += 1
                jogador[chaves] += dados
                print(jogador, dados, chaves, preso, temp, cont, flag)
                if jogador[chaves] > s:
                    break
            else:
                jogador[chaves] += dados
                print(jogador, dados, chaves, preso, temp, cont, flag)
                if jogador[chaves] > s:
                    print(chaves)
                    break
            chaves += 1
            if chaves > len(jogador):
                chaves = 1
            rodadas -= 1
        print(jogador)



if __name__ == "__main__":
    dado()


"""
2 10
2 4 8
4
1 1
3 4
1 2
6 5
3 7
4 5 7
7
1 2
2 2
2 1
1 1
1 2
1 1
1 1
0 0
"""