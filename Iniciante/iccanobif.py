def iccanobif():
    """
    Esta função calcula a sequência de fibonacci na ordem
    inversa.
    :return:
    """
    n = int(input())
    a, b = 0, 1
    l1, l2 = [], []
    for i in range(1, n + 1):
        a, b = b, a + b
        l1.append(a)
    l2 = l1[::-1].copy()
    print(*l2)


iccanobif()
