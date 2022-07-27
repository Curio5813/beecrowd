def main():
    """
    Escreva um programa que leia um valor inteiro N (1 < N < 1000). Este N é a quantidade de linhas de
    saída que serão apresentadas na execução do programa.
    """
    n = int(input())
    for k in range(1, n + 1):
        print(f'{k} {k ** 2} {k ** 3}')


if __name__ == '__main__':
    main()
