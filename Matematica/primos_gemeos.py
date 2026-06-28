def primos_gemeos():
    """
    Escreva um programa que dado um inteiro N, imprima os números
    primos gêmeos mais próximos menores ou iguais a N.

    De acordo com a wikipedia, "Um primo gêmeo é um número primo que
    é 2 a menos ou 2 a mais que outro número primo - por exemplo, qualquer
    membro do par primo gêmeo (41, 43). Em outras palavras, um primo gêmeo
    é primo que tem um intervalo de dois ".

    Entrada
    A entrada deve conter um inteiro N, em que (5 ≤ N ≤ 1000).

    Saída
    A saída deve conter dois inteiros X e Y separados por espaço, representando
    os dois números primos gêmeos mais próximos menores ou iguais a N.
    :return:
    """
    n = int(input())
    primos = []
    i = 2
    for i in range(i, n + 1):
        for k in range(2, n + 1):
            if i % k == 0 and i != k:
                i += 1
                break
            if i == k:
                primos.append(i)
                i += 1
                break
    primos.reverse()
    for i in range(0, len(primos)):
        if abs(primos[i] - primos[i + 1]) == 2:
            print(primos[i + 1], primos[i])
            break


primos_gemeos()
