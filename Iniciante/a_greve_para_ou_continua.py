def a_greve_para_ou_continua():
    """
    Esta função recebe como entradas N, que representa o numeros de valores
    citados na reunião da Universidade e os caracteres 'V' e 'G' separados
    por um espaço com valor inteiro 'C' (<= 1 C <= 100.000). Caso os valores
    de G seja menor que V, o programa deve imprimir "A greve vai parar.", caso
    contrário, deve ser impresso "NAO VAI TER CORTE, VAI TER LUTA!"
    :return:
    """
    n = int(input())
    gastos, governo = 0, 0
    for i in range(n):
        t, c = input().split(" ")
        c = int(c)
        if t == "V":
            governo += c
        elif t == "G":
            gastos += c
    if governo >= gastos:
        print("A greve vai parar.")
    elif governo < gastos:
        print("NAO VAI TER CORTE, VAI TER LUTA!")


a_greve_para_ou_continua()
