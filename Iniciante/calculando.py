def calculando():
    """
    Esta função printa o valor de uma expressão de adição e subtração
    de números dados como parâmetros de entrada.
    :return:
    """
    m, resul, cont = 1, 0, 0
    while m != 0:
        m = int(input())
        if m == 0:
            break
        cont += 1
        exp_postivo = list(map(int, input().split('+')))
        print(exp_postivo)


calculando()
