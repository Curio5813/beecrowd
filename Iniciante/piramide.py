

def piramide():
    """
    Esta função calcula e printa o menor valor dos pesos de cada
    caixa que formam um triangulo, baseado na matriz n x n dada.
    :return:
    """
    n = int(input())
    l1, l2, soma, m = [], [], 0, n
    for i in range(0, n):
        l1 = list(map(int, input().split(" ")))
        l2.append(l1)
    l2.reverse()
    print(l2)
    for k in range(0, len(l2)):
        for j in range(0, len(l2[k])):
            if k == 0:
                soma = sum(l2[k])
    print(soma)


piramide()
