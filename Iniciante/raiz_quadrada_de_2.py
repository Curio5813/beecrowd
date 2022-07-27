def main():
    """
    Uma das formas de calcular a raiz quadrada de um número natural é pelo método das
    frações periódicas continuadas. Esse método usa como denominador uma repetição de
    frações. Essa repetição pode ser feita uma quantidade específica de vezes.

             sqrt(2) ~ 1 + 1 / (2 + 1/2)

    Por exemplo, ao repetir 2 vezes a fração continuada para calcular a raiz quadrada
    de 2, temos a fórmula abaixo.

    Sua tarefa é, dado o número N de repetições, calcular o valor aproximado da raiz
    quadrada de 2.

    Entrada
    A entrada é um número natural N (0 ≤ N ≤ 100), que indica o número de repetições
    do denominador na fração continuada.

    Saída
    A saída é o valor aproximado da raiz quadrada com 10 casas decimais.
    """
    sqrt_2, numerador, denominador = 1, 1, 2
    n = int(input())
    for k in range(n):
        if k >= 1:
            denominador = 2 + 1 / denominador
        sqrt_2 = 1 + (numerador / denominador)
    print(f'{sqrt_2:.10f}')


if __name__ == '__main__':
    main()
