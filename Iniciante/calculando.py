def calculando():
    """
    Esta função printa o valor de uma expressão de adição e subtração
    de números dados como parâmetros de entrada.
    :return:
    """
    m, numeros, num, signal, soma, n = '1', [], "", [], 0, 1
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
        if len(numeros) == 1:
            print(f"Teste {n}")
            print(numeros[0])
            print("")
        else:
            for i in range(0, len(signal)):
                if i >= len(signal) - 1 and len(signal) < 2:
                    if signal[i] == '+':
                        soma = numeros[0] + numeros[1]
                        break
                    elif signal[i] == '-':
                        soma = numeros[0] - numeros[1]
                        break
                if i >= len(signal) - 1 and len(signal) >= 2:
                    if signal[i] == '+':
                        soma += numeros[i + 1]
                        break
                    elif signal[i] == '-':
                        soma += -numeros[i + 1]
                        break
                if i == 0:
                    if signal[i] == '+':
                        soma = numeros[0] + numeros[1]
                    elif signal[i] == '-':
                        soma = numeros[0] - numeros[1]
                elif i > 0:
                    if signal[i] == '+':
                        soma += numeros[i + 1]
                    elif signal[i] == '-':
                        soma += -numeros[i + 1]
            print(f"Teste {n}")
            print(soma)
            print("")
        n += 1
        numeros, num, signal, soma = [], "", [], 0


calculando()
