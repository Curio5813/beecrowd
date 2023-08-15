import math


def jogo_das_aranhas():
    """
    Esta função calcula e imprime um inteiro positivo k < 10^16,
    que satisfaz o jogo das aranhas criados por Arthur e Merlin,
    onde somente as aranhas-marrons venenosas são mortas, que
    estão dipostas em um circulo com com as inofensivas
    aranhas-vermelhas, dado como entrada um numero inteiro
    que é número de aranhas-marrons e, por conseguinte, de
    aranhas vermelhas, sendo que as aranhas-marrons vêm primereiro
    no círculo. Merlin tem que dizer um número onde somente as aranhas-marrons
    são mortas, para assim, vencer o jogo. Um vez morta uma aranhas, deves-se
    contar somente com as aranhas restantes.
    :return:
    """
    n = int(input())
    total = n * 2
    v = int(total / 2 + 1)
    prod = 1
    for i in range(v, total + 1):
        prod *= i
    print(prod)


jogo_das_aranhas()
