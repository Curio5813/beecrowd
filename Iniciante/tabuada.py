def main():
    """
    Leia 1 valor inteiro N (2 < N < 1000). A seguir, mostre a tabuada de N:
    1 x N = N      2 x N = 2N        ...       10 x N = 10N
    """
    n = int(input())
    while n < 2 or n > 1000:
        n = int(input())
    for k in range(1, 11):
        print(f'{k} x {n} = {k * n}')


if __name__ == '__main__':
    main()
