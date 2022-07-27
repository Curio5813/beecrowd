def main():
    """
    A fórmula de Binet é uma forma de calcular números de Fibonacci.


        Fibonacci(n) ~ (((1 + sqrt(5) / 2) ^ n - (1 - sqrt(5) / 2) ^ n) / sqrt(5)

    Sua tarefa é, dado um natural n, calcular o valor de Fibonacci(n) usando a fórmula acima.

    Entrada
    A entrada é um número natural n (0 < n ≤ 50).

    Saída
    A saída é o valor de Fibonacci(n) com 1 casa decimal utilizando a fórmula de Binet dada.
    """
    n = int(input())
    fibo = (((1 + 5 ** (1/2)) / 2) ** n - ((1 - 5 ** (1/2)) / 2) ** n) / 5 ** (1/2)
    print(f'{fibo:.1f}')


if __name__ == '__main__':
    main()
