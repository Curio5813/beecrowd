def xadrez():
    """
    Esta função printa, como resultado, o numero 1 se a cor da casa do canto
    inferior direito do tabuleiro pintado em forma de xadrez for branca, ou 0
    se for de cor preta. O tabuleiro pode ter suas dimensões com um numero de
    linhas entre 1 <= l <= 1_000 e colunas entre 1 <= c <= 1_000.
    :return:
    """
    lin = int(input())
    col = int(input())
    l1, n, casa = [], 0, 0
    for i in range(1, lin + 1):
        if i % 2 != 0:
            l1.append(1)
        if i % 2 == 0:
            l1.append(0)
    while n < col:
        casa = l1[-1]
        if l1[-1] == 0:
            l1[-1] = 1
        elif l1[-1] == 1:
            l1[-1] = 0
        n += 1
    print(casa)


xadrez()
