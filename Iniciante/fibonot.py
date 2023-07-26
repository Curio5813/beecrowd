def fibonot():
    """
    Esta função retorna o k-ésimo termo da sequência de
    fibonot, dado pelo seu indice como entrada do programa,
    que são formados pela sequência de números que não
    pertencem a sequência de fibonacci.
    :return:
    """
    fibo, fibo_not = [], []
    a, b = 0, 1
    for i in range(25):
        if a >= 100_000:
            break
        a, b = b, b + a
        fibo.append(a)
    for i in range(1, 100_100):
        if i not in fibo:
            fibo_not.append(i)
    k = int(input())
    print(fibo_not[k - 1])


fibonot()
