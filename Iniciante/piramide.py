def piramide():
    """
    Esta função calcula e printa o menor valor dos pesos de cada
    caixa que formam um triangulo, baseado na matriz n x n dada.
    :return:
    """
    n = int(input())
    l1, l2, soma, m = [], [], [], 1
    for i in range(0, n):
        l1 = list(map(int, input().split(" ")))
        l2.append(l1)
    print(l2)
    for k in range(0, len(l2)):
        for j in range(0, len(l2[k])):
            soma += l2[k][0:m]
            break
        m += 1
    print(soma)
    print(sum(soma))


piramide()
