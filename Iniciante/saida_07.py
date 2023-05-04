def saida7():
    """
    Esta função apenas printa valores relacionados de forma
    crescente com as letras do alfabeto.
    :return:
    """
    l1, n = [], 0
    for i in "abcdefghijklmnopqrstuvwxyz":
        l1.append(i)
    for i in range(97, 123):
        print(f"{i} e {l1[n]}")
        n += 1


saida7()

