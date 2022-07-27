def main():
    """
    Leia um caractere maiúsculo, que indica uma operação que deve ser realizada e uma matriz
    M[12][12]. Em seguida, calcule e mostre a soma ou a média considerando somente aqueles
    elementos que estão acima da diagonal principal da matriz, conforme ilustrado abaixo
    (área verde).
    """
    matriz, soma, n, a, x = [], [], 0, 0, 0
    t = input().upper()
    for linha in range(12):
        for coluna in range(12):
            valor = float(input())
            matriz.append(valor)
    if t == 'S':
        for i in range(12):
            n += 1 + a
            for k in range(n, 12 + a * x):
                soma.append(matriz[k])
            a = 12
            x += 1
        print(f'{sum(soma):.1f}')
    elif t == 'M':
        for i in range(12):
            n += 1 + a
            for k in range(n, 12 + a * x):
                soma.append(matriz[k])
            a = 12
            x += 1
        print(f'{sum(soma) / len(soma):.1f}')


if __name__ == '__main__':
    main()
