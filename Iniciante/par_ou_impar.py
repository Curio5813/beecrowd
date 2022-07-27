def main():
    """
    Leia um valor inteiro N. Este valor será a quantidade de valores que serão lidos em seguida. Para
    cada valor lido, mostre uma mensagem em inglês dizendo se este valor lido é par (EVEN), ímpar (ODD),
    positivo (POSITIVE) ou negativo (NEGATIVE). No caso do valor ser igual a zero (0), embora a descrição
    correta seja (EVEN NULL), pois por definição zero é par, seu programa deverá imprimir apenas NULL.
    """
    n = int(input())
    while n > 10_000:
        n = int(input())
    for k in range(0, n):
        num = int(input())
        if num % 2 == 0 and num > 0:
            print('EVEN POSITIVE')
        elif num % 2 == 0 and num < 0:
            print('EVEN NEGATIVE')
        elif num % 2 == 1 and num > 0:
            print('ODD POSITIVE')
        elif num % 2 == 1 and num < 0:
            print('ODD NEGATIVE')
        elif num == 0:
            print('NULL')


if __name__ == '__main__':
    main()
