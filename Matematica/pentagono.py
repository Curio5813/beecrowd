from math import tan, sqrt, radians


def pentagono():
    """
    É possível calcular a área de um pentágono regular, ou seja, uma
    figura geométrica com cinco lados iguais, dado o comprimento de
    um dos lados. Sendo assim, calcule.

    Escreva um programa que, dado o comprimento de um lado de um pentágono
    regular, calcule a sua área.

    Entrada
    Haverá um valor C que indica a quantidade de casos de teste. Em seguida,
    haverá um número inteiro N para cada caso (1 ≤ N ≤ 10000), indicando o
    comprimento do lado de um pentágono regular.

    Saída
    Para cada caso de teste, imprima o valor correspondente da área do respectivo
    pentágono, com três casas decimais de precisão.
    :return:
    """
    c = int(input())
    for i in range(c):
        n = int(input())
        area_petagono = (n ** 2 * sqrt(5)) / (4 * tan(radians(18)))
        print(f"{area_petagono:.3f}")


pentagono()
