def main():
    from math import factorial
    """
    Ler um valor N. Calcular e escrever seu respectivo fatorial. Fatorial de N = N * (N-1) * (N-2) * (N-3)
    * ... * 1.
    """
    n = int(input())
    x = factorial(n)
    print(x)


if __name__ == '__main__':
    main()
