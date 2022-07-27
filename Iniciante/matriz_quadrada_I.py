def main():
    """
    Escreva um algoritmo que leia um inteiro N (0 ≤ N ≤ 100), correspondente a ordem de uma
    matriz M de inteiros, e construa a matriz de acordo com o exemplo abaixo.
    """
    matriz, n = [], 1
    o = int(input())
    while o != 0:
        for k in range(o * o):
            matriz.append(k)
        print(matriz)
        for k in range(0, len(matriz)):
            if n % o == 0:
                print('\n')
            n += 1
            if o * n < matriz[k] < o * (n + 1) - 1:
                print(f'2   ', end='')
            else:
                print(f'1   ', end='')
        o = int(input())


if __name__ == '__main__':
    main()
