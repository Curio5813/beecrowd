from math import factorial


def a_grande_festa():
    """
    Famoso viajante interplanetário, ET Bilu quer convidar pessoas do planeta
    que está visitando para uma Grande Festa. Na cultura de Bilu, uma festa só
    pode ser considerada uma Grande Festa se pelo menos dois participantes tenham
    nascido no mesmo dia.

    Diferente do planeta Terra, que cada ano tem 365 ou 366 dias, os planetas que
    Bilu visita possuem uma quantidade de dias diferentes.

    Mesmo com toda a avançada tecnologia de viagem intergalática, Bilu não sabe
    calcular a chance de desse grande evento acontecer. Sendo assim, você, que estava
    em uma Grande Festa realizada no planeta Terra, irá ajudar Bilu a incorporar no
    computador de borda da nave um programa para estimar a chance de acontecer uma
    Grande Festa.

    Dado a quantidade de dias por ano do planeta que Bilu está visitando e a quantidade
    de pessoas na festa, determine a probabilidade da festa ser considerada uma Grande Festa.

    Entrada
    A entrada consiste em dois inteiros D e P indicando a quantidade de dias e de pessoas,
    respectivamente.

    Limites:

    50 <= D <= 10^5;

    2 <= P <= D - 1.

    Saída
    A saída deve ser a porcentagem de chance do evento ser uma Grande Festa com duas casas
    decimais.
    :return:
    """
    d, p = map(int, input().strip().split(" "))
    # Formula para o cálculo do Paradoxo do Aniversário.
    probabilidade = (1 - (factorial(d) / ((d ** p) * factorial(d - p)))) * 100
    print(f"{probabilidade:.2f}")


a_grande_festa()
