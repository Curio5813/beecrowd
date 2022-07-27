def main():
    """
     Leia um caractere maiúsculo, que indica uma operação que deve ser realizada e uma
     matriz M[12][12]. Em seguida, calcule e mostre a soma ou a média considerando
     somente aqueles elementos que estão acima da diagonal secundária da matriz,
     conforme ilustrado abaixo (área verde).
    """
    matriz, soma, a, b, x = [], [], 0, 0, 1
    o = input().upper()
    for linha in range(12):
        for coluna in range(12):
            valor = float(input())
            matriz.append(valor)
    if o == 'S':
        for k in range(12):
            b -= 1
            for i in range(a, 12 * x + b):
                soma.append(matriz[i])
            x += 1
            a += 12
        print(f'{sum(soma):.1f}')
    elif o == 'M':
        for k in range(12):
            b -= 1
            for i in range(a, 12 * x + b):
                soma.append(matriz[i])
            x += 1
            a += 12
        print(f'{(sum(soma) / len(soma)):.1f}')


if __name__ == '__main__':
    main()
