def main():
    """
    Leia um conjunto não determinado de pares de valores M e N (parar quando algum dos valores for
    menor ou igual a zero). Para cada par lido, mostre a sequência do menor até o maior e a soma
    dos inteiros consecutivos entre eles (incluindo o N e M).
    """
    while True:
        sequencia = []
        m, n = input().split(' ')
        m, n = int(m), int(n)
        if m <= 0 or n <= 0:
            break
        else:
            if m >= n:
                for k in range(n, m + 1):
                    sequencia.append(k)
                print(*sequencia, end=' ')
                print(f'Sum={sum(sequencia)}')
            elif n >= m:
                for k in range(m, n + 1):
                    sequencia.append(k)
                print(*sequencia, end=' ')
                print(f'Sum={sum(sequencia)}')


if __name__ == '__main__':
    main()
