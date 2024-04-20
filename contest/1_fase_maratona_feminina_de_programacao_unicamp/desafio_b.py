def desafio_b():
    dados = list(map(int, input().split(" ")))
    m, n = dados[0], dados[1]
    a = m ** 2 - n ** 2
    b = 2 * m * n
    c = m ** 2 + n ** 2
    print(a, b, c)


desafio_b()
