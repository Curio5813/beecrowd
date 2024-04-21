def desafio_a():
    n = int(input())
    moedas, passo1, passo2 = 0, 0, 0
    postos = list(map(int, input().split(" ")))
    if n % 2 == 0:
        postos.insert(0, 0)
        moedas = postos[1]
        i = 1
        while i < 2 ** (n - 1) or i <= len(postos) - 1:
            passo1 = 2 * i
            passo2 = 2 * i + 1
            if passo1 >= len(postos) - 1 or passo1 >= len(postos):
                break
            if postos[passo1] >= postos[passo2]:
                moedas += postos[passo1]
                i += passo1
            if postos[passo1] < postos[passo2]:
                moedas += postos[passo2]
                i += passo2
    if n % 2 == 1:
        i = 0
        moedas = postos[0]
        while i < 2 ** (n - 1) or i <= len(postos) - 1:
            passo1 = 2 * i
            passo2 = 2 * i + 1
            if passo1 >= len(postos) - 1 or passo1 >= len(postos):
                break
            if postos[passo1] >= postos[passo2]:
                moedas += postos[passo1]
                i += passo1
            if postos[passo1] < postos[passo2]:
                moedas += postos[passo2]
                i += passo2
    total = moedas
    print(total)


desafio_a()
