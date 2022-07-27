def main():
    """
    A seguinte sequência de números 0 1 1 2 3 5 8 13 21... é conhecida como série de Fibonacci. Nessa
    sequência, cada número, depois dos 2 primeiros, é igual à soma dos 2 anteriores. Escreva um
    algoritmo que leia um inteiro N (N < 46) e mostre os N primeiros números dessa série.
    """
    a, b, = 0, 1
    n = int(input())
    for k in range(1, n + 1):
        print(f'{a}', end=' ')
        a, b = b, a + b


if __name__ == '__main__':
    main()
