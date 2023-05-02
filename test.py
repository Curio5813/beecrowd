def sequencia_de_fibonacci():
    """
    Esta função retorna uma lista com a Sequencias de Fibonnaci.
    :return:
    """
    l1, m, n, p = [], 0, 1, 1
    for i in range(0, 25_000 + 1):
        l1.append(m)
        m = n
        n = p
        p = m + n
    return print(l1)


sequencia_de_fibonacci()
