def main():
    """
    Escreva um algoritmo que leia um inteiro N (0 ≤ N ≤ 15), correspondente a ordem de uma matriz M de
    inteiros, e construa a matriz de acordo com o exemplo abaixo.
    """
    o = int(input())
    while o != 0:
        matriz, n, m = [], 0, 1
        for lin in range(o):
            for col in range(o):
                if lin == 0:
                    matriz.append(2 ** n)
                    n += 1
                elif lin > 0:
                    n = lin
                    matriz.append(2 ** n)
                    lin += 1
        if o <= 2:
            for k in range(0, len(matriz)):
                if m % o == 0:
                    print(f'{matriz[k]:}')
                else:
                    print(f'{matriz[k]:}', end=' ')
                m += 1
        elif 3 <= o <= 4:
            for k in range(0, len(matriz)):
                if m % o == 0:
                    print(f'{matriz[k]:>2}')
                else:
                    print(f'{matriz[k]:>2}', end=' ')
                m += 1
        elif o == 5:
            for k in range(0, len(matriz)):
                if m % o == 0:
                    print(f'{matriz[k]:>3}')
                else:
                    print(f'{matriz[k]:>3}', end=' ')
                m += 1
        elif 6 <= o <= 7:
            for k in range(0, len(matriz)):
                if m % o == 0:
                    print(f'{matriz[k]:>4}')
                else:
                    print(f'{matriz[k]:>4}', end=' ')
                m += 1
        elif 8 <= o <= 9:
            for k in range(0, len(matriz)):
                if m % o == 0:
                    print(f'{matriz[k]:>5}')
                else:
                    print(f'{matriz[k]:>5}', end=' ')
                m += 1
        elif o == 10:
            for k in range(0, len(matriz)):
                if m % o == 0:
                    print(f'{matriz[k]:>6}')
                else:
                    print(f'{matriz[k]:>6}', end=' ')
                m += 1
        elif 11 <= o <= 12:
            for k in range(0, len(matriz)):
                if m % o == 0:
                    print(f'{matriz[k]:>7}')
                else:
                    print(f'{matriz[k]:>7}', end=' ')
                m += 1
        elif 13 <= o <= 14:
            for k in range(0, len(matriz)):
                if m % o == 0:
                    print(f'{matriz[k]:>8}')
                else:
                    print(f'{matriz[k]:>8}', end=' ')
                m += 1
        elif o == 15:
            for k in range(0, len(matriz)):
                if m % o == 0:
                    print(f'{matriz[k]:>9}')
                else:
                    print(f'{matriz[k]:>9}', end=' ')
                m += 1
        print('')
        o = int(input())


if __name__ == '__main__':
    main()
