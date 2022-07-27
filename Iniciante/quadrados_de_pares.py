def main():
    """
    Leia um valor inteiro N. Apresente o quadrado de cada um dos valores pares, de 1 até N, inclusive N,
    se for o caso.
    """
    n = int(input())
    while n < 5 or n > 2_000:
        n = int(input())
    pares = [k for k in range(2, n + 1) if k % 2 == 0]
    for k in pares:
        quadrado = k ** 2
        print(f'{k}^2 = {quadrado}')


if __name__ == '__main__':
    main()
