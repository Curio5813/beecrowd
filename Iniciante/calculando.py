def calculando():
    """
    Esta função printa o valor de uma expressão de adição e subtração
    de números dados como parâmetros de entrada.
    :return:
    """
    m, i, numeros, num, signal, n = '1', 0, [], "", [], 0
    while m != '0':
        m = input()
        if m == '0':
            break
        x = input()
        for i in range(0, len(x)):
            if i == len(x) - 1:
                num += x[i]
                numeros.append(int(num))
            if x[i] == '+' or x[i] == '-':
                numeros.append(int(num))
                signal.append(x[i])
                num = ""
            elif x[i] in "0123456789":
                num += x[i]


calculando()
