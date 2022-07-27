def main():
    """
    Escreva um programa que leia dois valores X e Y. A seguir, mostre uma sequência de 1 até Y, passando
    para a próxima linha a cada X números.
    """
    n, k = 1, 1
    x, y = input().split(' ')
    x, y = int(x), int(y)
    while k < y:
        while k <= x * n and y >= k:
            print(k, end=' ')
            k += 1
            if k == x * n:
                print(k, end='')
                print('')
                k += 1
                break
        n += 1


if __name__ == '__main__':
    main()
