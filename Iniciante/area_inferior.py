def main():
    """
    Leia um caractere maiúsculo, que indica uma operação que deve ser realizada e uma
    matriz M[12][12]. Em seguida, calcule e mostre a soma ou a média considerando
    somente aqueles elementos que estão na área inferior da matriz, conforme ilustrado
    abaixo (área verde).
    """
    matriz, soma, a, b, c, d = [], [], 7, 0, 7, 0
    o = input().upper()
    for linha in range(12):
        for coluna in range(12):
            valor = float(input())
            matriz.append(valor)
    if o == 'S':
        for k in range(12):
            for i in range(12 * a + 5 - b, 12 * c + 7 + d):
                if i >= len(matriz):
                    break
                soma.append(matriz[i])
            a += 1
            b += 1
            c += 1
            d += 1
        print(f'{sum(soma):.1f}')
    elif o == 'M':
        for k in range(12):
            for i in range(12 * a + 5 - b, 12 * c + 7 + d):
                if i >= len(matriz):
                    break
                soma.append(matriz[i])
            a += 1
            b += 1
            c += 1
            d += 1
        print(f'{sum(soma)/ len(soma):.1f}')


if __name__ == '__main__':
    main()
