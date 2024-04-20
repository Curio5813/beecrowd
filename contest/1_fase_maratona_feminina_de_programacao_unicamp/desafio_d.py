def desafio_d():
    n = int(input())
    cont = 0
    while n >= 8:
        n -= 8
        cont += 1
    while n >= 4:
        n -= 4
        cont += 1
    while n >= 2:
        n -= 2
        cont += 1
    while n >= 1:
        n -= 1
        cont += 1
    print(cont)


desafio_d()
