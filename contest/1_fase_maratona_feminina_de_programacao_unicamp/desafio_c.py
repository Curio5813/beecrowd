def desafio_c():
    pares, distancias = [], []
    for i in range(4):
        par = list(map(int, input().split(" ")))
        pares.append(par)
    for i in range(0, len(pares)):
        distancias.append(((pares[i][0] - pares[i - 1][0]) ** 2 + (pares[i][1] - pares[i - 1][1]) ** 2) ** (1/2))
    area = int(min(distancias) * min(distancias))
    print(area)


desafio_c()
