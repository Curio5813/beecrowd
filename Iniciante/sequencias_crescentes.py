def main():
    """
    Este programa deve ler uma variável inteira X inúmeras vezes (deve parar quando o valor no arquivo de
    entrada for igual a zero). Para cada valor lido imprima a sequência de 1 até X, com um espaço entre
    cada número e seu sucessor.
    """
    x = int(input())
    while x != 0:
        for k in range(1, x + 1):
            if k == x:
                print(x, end='')
                break
            print(k, end=' ')
        print('')
        x = int(input())


if __name__ == '__maina__':
    main()
