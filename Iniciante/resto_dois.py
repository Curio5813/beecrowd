def main():
    """
    Leia um valor inteiro N. Apresente todos os números entre 1 e 10000 que divididos por N dão resto
    igual a 2.
    """
    n = int(input())
    while n < 1 or n >= 10_000:
        n = int(input())
    for k in range(1, 10_000):
        if k % n == 2:
            print(k)


if __name__ == '__main__':
    main()
