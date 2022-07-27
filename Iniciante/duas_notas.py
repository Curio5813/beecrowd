def main():
    """
    Gilberto é um famoso vendedor de esfirras na região. Porém, apesar de todos
    gostarem de suas esfirras, ele só sabe dar o troco com duas notas, ou seja,
    nem sempre é possível receber o troco certo. Para facilitar a vida de Gil,
    escreva um programa para ele que determine se é possível ou não devolver o
    troco exato utilizando duas notas.

    As notas disponíveis são: 2, 5, 10, 20, 50 e 100.

    Entrada
    A entrada deve conter o valor inteiro N da compra realizada pelo cliente e,
    em seguida, o valor inteiro M pago pelo cliente (N < M ≤ 104). A entrada
    termina com N = M = 0.

    Saída
    Seu programa deverá imprimir "possible" se for possível devolver o troco exato
    ou "impossible" se não for possível.
    """
    while True:
        notas, answer = [2, 5, 10, 20, 50, 100], {()}
        n, m = input().split()
        n, m = int(n), int(m)
        troco = m - n
        if n == 0 and m == 0:
            break
        if notas[0] + notas[1] == troco:
            print('possible')
        elif notas[0] + notas[2] == troco:
            print('possible')
        elif notas[0] + notas[3] == troco:
            print('possible')
        elif notas[0] + notas[4] == troco:
            print('possible')
        elif notas[0] + notas[5] == troco:
            print('possible')
        elif notas[1] + notas[2] == troco:
            print('possible')
        elif notas[1] + notas[3] == troco:
            print('possible')
        elif notas[1] + notas[4] == troco:
            print('possible')
        elif notas[1] + notas[5] == troco:
            print('possible')
        elif notas[2] + notas[3] == troco:
            print('possible')
        elif notas[2] + notas[4] == troco:
            print('possible')
        elif notas[2] + notas[5] == troco:
            print('possible')
        elif notas[3] + notas[4] == troco:
            print('possible')
        elif notas[3] + notas[5] == troco:
            print('possible')
        elif notas[4] + notas[5] == troco:
            print('possible')
        else:
            print('impossible')


if __name__ == '__main__':
    main()
