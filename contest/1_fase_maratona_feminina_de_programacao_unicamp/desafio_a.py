def desafio_a():
    n = int(input())
    passo1, passo2, moedas1, moedas2, totais = 0, 0, 0, 0, []
    postos = list(map(int, input().split(" ")))
    postos.insert(0, 0)
    moedas = postos[1]
    moedas1 += moedas
    moedas2 += moedas
    i = 1
    j = 1
    t = 1
    u = 1
    k = (2 ** n) - 1
    while i < k or j < k:
        i *= 2
        j = 2 * j + 1
        t *= 2
        u = 2 * u + 1
        if postos[i] >= postos[j]:
            moedas += postos[i]
            j = i
        if postos[i] < postos[j]:
            moedas += postos[j]
            i = j
        moedas1 += postos[t]
        moedas2 += postos[u]
    total1 = moedas
    total2 = moedas1
    total3 = moedas2
    totais.append(total1)
    totais.append(total2)
    totais.append(total3)
    print(max(totais))


desafio_a()
