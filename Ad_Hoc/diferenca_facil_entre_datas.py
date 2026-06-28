from datetime import datetime


def diferenca_facil_entre_datas():
    """
    Seu programa deve ler duas datas (dia e mês) e calcular a diferença
    entre elas, em dias. Considere se tratar de um ano não bissexto (fevereiro
    com 28 dias).

    Entrada
    A entrada contem duas linhas contendo dois inteiros cada, representando o
    dia e o mês da primeira e da segunda data. A primeira data será sempre menor
    (anterior no ano) ou igual à segunda.

    Saída
    A saída deverá conter o número de dias entre a primeira e a segunda data.
    :return:
    """
    dia1, mes1 = map(int, input().split(" "))
    dia2, mes2 = map(int, input().split(" "))
    ano = 2023
    data1 = datetime(ano, mes1, dia1)
    data2 = datetime(ano, mes2, dia2)
    diff_dias = data2 - data1
    dias = diff_dias.days
    print(dias)


diferenca_facil_entre_datas()
