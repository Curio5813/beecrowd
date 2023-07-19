from math import ceil, floor


def keanu():
    """
    Esta função calcula quantas casa brancas e quantas casa pretas
    há em tabuleiros de xadrez de diferentes comprimento.
    :return:
    """
    n = int(input())
    if n % 2 != 0:
        casas = n * n
        a = ceil(casas / 2)
        b = floor(casas / 2)
        print(f"{a} casas brancas e {b} casas pretas")
    elif n % 2 == 0:
        casas = n * n
        a = int(casas / 2)
        b = a
        print(f"{a} casas brancas e {b} casas pretas")


keanu()
