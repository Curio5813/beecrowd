def main():
    """
    Escreva um algoritmo que leia um inteiro N (0 ≤ N ≤ 100), correspondente a ordem de uma matriz M de
    inteiros, e construa a matriz de acordo com o exemplo abaixo.
    """
    o = int(input())
    while o != 0:
        matriz, n, d, c, m = [], 1, 2, 1, 1
        for lin in range(o):
            for col in range(o):
                if col > lin:
                    n += 1
                elif col < lin:
                    n -= 1
                else:
                    n = 0
                    c = 1
                    n += c
                matriz.append(n)
            d += 1
            n = d
        for k in range(0, len(matriz)):
            if m % o == 0:
                print(f'{matriz[k]:>3}')
            else:
                print(f'{matriz[k]:>3}', end=' ')
            m += 1
        print('')
        o = int(input())


if __name__ == '__main__':
    main()
