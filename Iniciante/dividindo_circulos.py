from math import factorial


def dividindo_circulos():
    """
    Esta função calcula o numeros de partes que um circulo
    pode ter a partir da quantidade de segmentos ligados
    por pares de pontos que se encontram em cima da circunferência.
    :return:
    """
    # Formula Geral: r = 1 + C(n, 2) + C(n, 4)
    n = int(input())
    if n <= 5:
        r = 2 ** (n - 1)
        print(r)
    elif n > 5:
        r = int(1 + factorial(n) / (factorial(n - 2) * 2) + factorial(n) / (factorial(n - 4) * factorial(4)))
        print(r)


dividindo_circulos()
