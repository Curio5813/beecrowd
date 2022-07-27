def main():
    """
    Na matemática, um Número Primo é aquele que pode ser dividido somente por 1 (um) e por ele mesmo.
    Por exemplo, o número 7 é primo, pois pode ser dividido apenas pelo número 1 e pelo número 7.
    """
    n = int(input())
    div = 3
    for k in range(0, n):
        x = int(input())
        if x == 2:
            print(f'{x} eh primo')
        elif x == 3:
            print(f'{x} eh primo')
        elif x > 3 and x % 2 != 0:
            while x % div != 0:
                div += 1
                if div == x:
                    print(f'{x} eh primo')
                    break
            else:
                print(f'{x} nao eh primo')
        elif x % 2 == 0:
            print(f'{x} nao eh primo')
        div = 3


if __name__ == '__main__':
    main()
