def mais_um_joguinho():
    """
    Fingolfin adora jogos de tabuleiro. Certo dia, se depara com
    um jogo muito estranho chamado “2 Primeiros Primos”. Basicamente
    este jogo consistia em um tabuleiro de uma única linha na horizontal
    que contém N casas. O jogador inicia na casa de número 1 e o objetivo
    é chegar a casa N (não podendo ultrapassar). Em cada rodada, o jogador
    pode se movimentar de duas formas: andar 2 ou 3 casas para frente (oh
    sim, agora faz sentido o título do jogo).

    Fingolfin achou o jogo muito fácil (só andar pra frente), então seu colega
    Fëanor lhe desafia a dizer quantas possibilidades distintas existem de ele
    terminar o jogo, ou seja, de quantas formas distintas Fingolfin, a partir
    da casa 1, consegue chegar à casa N.

    Fingolfin está um pouco ocupado cuidando de alguns afazeres de casa e pediu
    para você que, dado o número de casas do tabuleiro, resolva o desafio.

    Entrada
    Inteiro N(1 ≤ N ≤ 105), indicando o número de casas do tabuleiro.

    Saída
    Inteiro indicando o número de possibilidades de terminar o jogo. O número de
    possibilidades pode ser muito grande, então deve-se mostrar apenas o valor de
    resto deste valor ao ser dividido por 10^9 + 7.
    :return:
    """
    p, possibilidades = 10 ** 9 + 7, 0
    n = int(input())
    if n == 1:
        return print(0)
    if n == 2:
        return print(1)
    if n == 3:
        return print(1)
    if n == 4:
        return print(1)
    if n == 5:
        return print(2)
    else:
        passos1 = 1
        passos2 = 1
        passos3 = 1
        for i in range(6, n + 1):
            possibilidades = passos2 + passos3
            passos3 = passos2
            passos2 = passos1
            passos1 = possibilidades
        print(possibilidades % p)


mais_um_joguinho()
