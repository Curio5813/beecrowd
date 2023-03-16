def domino():
    """
    Esta função printa quantas peças tem um dominó com um
    número máximo (n).
    """
    n = int(input())
    p = ((n + 1) * (n + 2)) / 2
    print(int(p))


domino()
