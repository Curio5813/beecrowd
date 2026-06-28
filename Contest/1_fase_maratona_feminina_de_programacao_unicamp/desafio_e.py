from math import ceil


def desafio_e():
    cont, aux = 0, 0
    n, p = map(int, input().split(" "))
    steam = list(map(int, input().split(" ")))
    steam.sort()
    media = ceil(sum(steam) / n)
    print(media)
    for i in range(0, len(steam)):
        cont += ceil(media / steam[i])
    if cont >= p:
        print(cont)
    else:
        for i in range(0, len(steam)):
            aux += steam[i]
            cont += 1
            if cont >= p:
                print(aux)
                break


desafio_e()
