def sucessor_par():
    """
    A função printa o menor sucessor par de um dado número.
    """
    x = int(input())
    if x % 2 == 0:
        print(x + 2)
    elif x % 2 == 1:
        print(x + 1)


sucessor_par()
