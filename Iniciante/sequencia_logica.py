def main():
    """
    Escreva um programa que leia um valor inteiro N. N * 2 linhas de saída serão apresentadas na execução
    do programa, seguindo a lógica do exemplo abaixo. Para valores com mais de 6 dígitos, todos os dígitos
    devem ser apresentados.
    """
    n = int(input())
    for k in range(1, n + 1):
        print(f'{k} {k * k} {k * k * k}\n'
              f'{k} {(k * k) + 1} {(k * k * k) + 1}')


if __name__ == '__main__':
    main()
