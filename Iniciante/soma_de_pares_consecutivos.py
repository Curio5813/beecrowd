def main():
    """
    O programa deve ler um valor inteiro X indefinidas vezes. (O programa irá parar quando o valor de
    X for igual a 0). Para cada X lido, imprima a soma dos 5 pares consecutivos a partir de X, inclusive
    o X , se for par. Se o valor de entrada for 4, por exemplo, a saída deve ser 40, que é o resultado
    da operação: 4+6+8+10+12, enquanto que se o valor de entrada for 11, por exempo, a saída deve ser
    80, que é a soma de 12+14+16+18+20.
    """
    soma = 0
    x = int(input())
    while x != 0:
        if x % 2 == 0:
            for i in range(x, 5 * 2 + x, 2):
                soma += i
        elif x % 2 == 1:
            for i in range(x + 1, 5 * 2 + x, 2):
                soma += i
        print(soma)
        soma = 0
        x = int(input())


if __name__ == '__main__':
    main()
