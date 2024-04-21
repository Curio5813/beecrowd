def desafio_a():
    n = int(input())
    passo1, passo2, moedas1, moedas2, totais = 0, 0, 0, 0, []
    postos = list(map(int, input().split(" ")))
    postos.insert(0, 0)
    print(postos)
    moedas = postos[1]
    moedas1 += moedas
    moedas2 += moedas
    i = 1
    j = 0
    k = 2 ** (n - 1)
    while passo1 < k or passo2 < k or i <= len(postos) - 1:
        passo1 = 2 * i
        passo2 = 2 * i + 1
        if passo1 >= len(postos) - 1 or passo1 >= len(postos) or passo1 > k + 1 or passo2 > k + 1:
            break
        if postos[passo1] >= postos[passo2]:
            moedas += postos[passo1]
            j += 1
            i = j
        if postos[passo1] < postos[passo2]:
            moedas += postos[passo2]
            j += 2
            i = j
        moedas1 += postos[passo1]
        moedas2 += postos[passo2]
    total1 = moedas
    total2 = moedas1
    total3 = moedas2
    totais.append(total1)
    totais.append(total2)
    totais.append(total3)
    print(totais)
    print(max(totais))


desafio_a()
