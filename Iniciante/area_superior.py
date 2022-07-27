def main():
    from decimal import Decimal
    """
    Leia um caractere maiúsculo, que indica uma operação que deve ser realizada e uma
    matriz M[12][12]. Em seguida, calcule e mostre a soma ou a média considerando
    somente aqueles elementos que estão na área superior da matriz, conforme ilustrado
    abaixo (área verde).
    """
    matriz, soma, a, b, c, d = [], [], 0, 0, 0, 0
    o = input().upper()
    for linha in range(12):
        for coluna in range(12):
            valor = float(Decimal(input()))
            matriz.append(valor)
    if o == 'S':
        for k in range(12):
            a += 1
            c += 1
            d -= 1
            for i in range(a + 12 * b, 12 * c + d):
                soma.append(matriz[i])
            b += 1
        print(f'{sum(soma):.1f}')
    elif o == 'M':
        for k in range(12):
            a += 1
            c += 1
            d -= 1
            for i in range(a + 12 * b, 12 * c + d):
                soma.append(matriz[i])
            b += 1
        print(f'{sum(soma) / len(soma):.1f}')


if __name__ == '__main__':
    main()
