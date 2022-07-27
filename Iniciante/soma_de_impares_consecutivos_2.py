def main():
    """
    Leia um valor inteiro N que é a quantidade de casos de teste que vem a seguir. Cada caso de
    teste consiste de dois inteiros X e Y. A função imprime a soma de todos os ímpares existentes
    entre X e Y.
    """
    n = int(input())
    for k in range(0, n):
        x, y = input().split(' ')
        x, y = int(x), int(y)
        if y <= x:
            impares = [k for k in range(y, x) if k > y and k % 2 != 0]
            print(f'{sum(impares)}')
        elif x <= y:
            impares = [k for k in range(x, y) if k > x and k % 2 != 0]
            print(f'{sum(impares)}')


if __name__ == '__main__':
    main()
