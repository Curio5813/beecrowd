from math import factorial


def cadeado_insano():
    """
    :return:
    """
    divisao = 109 + 7
    print(3456 % divisao)
    valor1, valor2 = 0, 0
    n, k = map(int, input().strip().split(" "))
    fixo = list(map(int, input().strip().split(" ")))
    movel = list(map(int, input().strip().split(" ")))
    for i in range(0, len(fixo)):
        valor1 += 2 ** fixo[i]
        valor2 += 2 ** movel[i]
    combinacoes = (factorial(valor1) / factorial(valor1 - 31)) / (factorial(valor2) / factorial(valor2 - 31))
    print(combinacoes)
    print(combinacoes % divisao)


cadeado_insano()
