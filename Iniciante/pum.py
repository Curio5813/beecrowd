def main():
    """
    Escreva um programa que leia um valor inteiro N. Este N é a quantidade de linhas de saída que serão
    apresentadas na execução do programa.
    """
    pum1, pum2, pum3 = 1, 2, 3
    n = int(input())
    for k in range(1, n + 1):
        print(f'{pum1} {pum2} {pum3} PUM')
        pum1 += 4
        pum2 += 4
        pum3 += 4


if __name__ == '__main__':
    main()
