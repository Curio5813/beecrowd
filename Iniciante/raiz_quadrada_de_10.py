def main():
    """
    Uma das formas de calcular a raiz quadrada de um número natural é pelo método
    das frações periódicas continuadas. Esse método usa como denominador uma
    repetição de frações. Essa repetição pode ser feita uma quantidade específica
    de vezes.

    Por exemplo, ao repetir 2 vezes a fração continuada para calcular a raiz quadrada
    de 10, temos a fórmula abaixo.

                    sqrt(10) ~ 3 + 1 / (6 + (1 / 6))

    Sua tarefa é, dado o número N de repetições, calcular o valor aproximado da raiz
    quadrada de 10.

    Entrada
    A entrada é um número natural N (0 ≤ N ≤ 100), que indica o número de repetições
    do denominador na fração continuada.

    Saída
    A saída é o valor aproximado da raiz quadrada com 10 casas decimais.
    """
    n = int(input())
    numero, numerador, denominador = 3, 1, 6
    for k in range(n):
        if k >= 1:
            denominador = 6 + 1 / denominador
        numero = 3 + (numerador / denominador)
    print(f'{numero:.10f}')


if __name__ == '__main__':
    main()
