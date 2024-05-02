def soma_ate_n():
    """
    Todos os números positivos podem ser expressos como a soma de um,
    dois ou mais números inteiros positivos consecutivos. Por exemplo,
    9 pode ser expresso em três diferentes formas, 2+3+4, 4+5 ou 9.
    Dado um número inteiro menor que (9*10^14+1) ou (9E14 + 1) ou
    (9*10¹⁴ +1), você terá que determinar de quantas maneiras este
    número pode ser expresso como a soma de números consecutivos.
    Entrada
    O arquivo de entrada contém menos de 1100 linhas de entrada (casos de teste).
    Cada caso de teste contém um inteiro N (0 ≤ N ≤ 9E14) . O final de entrada
    é determinado por EOF.

    Saída
    Para cada caso de teste produza uma linha de saída. Esta linha deverá conter
    um inteiro que informa de quantas maneiras N pode ser expresso como a soma
    de inteiros consecutivos.
    :return:
    """
    while True:
        try:
            n = int(input())
            soma, qt, inicio = 0, 0, 1
            if n == 0:
                print(1)
            if n == 1:
                print(1)
            if n > 1:
                for i in range(inicio, n + 1):
                    for k in range(i, n + 1):
                        soma += k
                        if soma == n:
                            qt += 1
                            break
                        if soma > n:
                            break
                    soma = 0
                    inicio += 1
                print(qt)
        except EOFError:
            break


soma_ate_n()
