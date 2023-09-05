def tomadas_eletricas():
    """
    Esta função calcula, para cada caso teste, o número de
    aparelhos que podem ser ligados em uma casa, que tem apenas
    uma tomada, através de réguas de energias, tendo como entradas
    do problema a quantidade de réguas de energia e a quantidade
    de tomadas que há em cada régua de energia.
    :return:
    """
    qt = 0
    n = int(input())
    for i in range(n):
        k = list(map(int, input().split(" ")))
        for j in range(1, len(k)):
            if j == len(k) - 1:
                qt += k[j]
                break
            qt += k[j] - 1
        print(qt)
        qt = 0


tomadas_eletricas()
