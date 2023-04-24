def desvendando_monty_hall():
    """
    Esta função calcula se, dado um numero de jogos Monty hall,
    quantas vezes o jogador ganhou, lenvando-se em consideração
    que sua primeira escolha será sempre a porta 1 e que ele
    sempre troca de porta, no caso, para porta 2 ou porta 3.
    :return:
    """
    n = int(input())
    cont = 0
    for i in range(n):
        winner_door = int(input())
        if winner_door != 1:
            cont += 1
    return print(cont)


desvendando_monty_hall()
