def desafio_a():
    n = int(input())
    i, moedas, passo, moedas1, moedas2 = 0, 0, 1, 0, 0
    postos = list(map(int, input().split(" ")))
    moedas = postos[0]
    for i in range(1, len(postos), passo):
        print(postos[passo])
        if i >= 2 ** (n - 1):
            print(f"ok{i}")
            break
        passo = 2 * i
        if passo <= len(postos) - 1:
            moedas1 += postos[passo]
    print("---------")
    for i in range(1, len(postos), passo):
        print(postos[passo])
        if i >= 2 ** (n - 1):
            print(f"ok{i}")
            break
        passo = 2 * i + 1
        if passo <= len(postos) - 1:
            moedas2 += postos[passo]
    total1 = moedas + moedas1
    total2 = moedas + moedas2
    # print(total1)
    # print(total2)
    if total1 >= total2:
        print(total1)
    if total1 < total2:
        print(total2)


desafio_a()
